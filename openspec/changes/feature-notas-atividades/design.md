# Design

## Context

No escopo do EduTrack AI, a funcionalidade de avaliação necessita de uma estrutura no backend (Xano) para que os docentes registrem as notas obtidas pelos estudantes em tarefas específicas.

Seguindo as diretrizes de escopo e arquitetura do [`AGENTS.md`](file:///c:/Users/2601914/Desktop/edutrack.ai/AGENTS.md), o planejamento cobre estritamente a criação da entidade no banco de dados e a rota de submissão da nota solicitada pelo usuário.

## Goals / Non-Goals

**Goals:**
- Projetar o schema da tabela `activity_grades` em XanoScript com relacionamento ao professor (`user_id`), aluno (`student_id`), atividade (`academic_task_id`) e a nota atribuída (`grade`).
- Especificar o endpoint `POST /activity_grades` com autenticação, validação de dados e inserção do registro.

**Non-Goals:**
- Endpoints de consulta, listagem ou cálculo de médias (ex.: GET /academic_tasks/{id}/grades, GET /users/{id}/grades), visto que não foram explicitamente solicitados.
- Interfaces de frontend ou relatórios analíticos nesta etapa.

## Decisions

### 1. Modelo de Banco de Dados (`activity_grades`)
- **Tabela:** `activity_grades`
- **Campos:**
  - `id`: `int` (Chave Primária, autoincrement)
  - `user_id`: `int` (Referência ao usuário autenticado - professor/avaliador)
  - `student_id`: `int` (Referência ao aluno avaliado)
  - `academic_task_id`: `int` (Referência à atividade avaliada)
  - `grade`: `decimal` (Valor da nota, ex.: min:0, max:10)
  - `feedback`: `text?` (Comentário opcional sobre a avaliação)
  - `created_at`: `timestamp` (Data de lançamento da nota)
- **Índices:**
  - Primary em `id`
  - Btree em `(academic_task_id, student_id)`
  - Btree em `user_id`

### 2. Endpoint REST (`POST /activity_grades`)
- **Rota:** `POST /activity_grades`
- **Autenticação:** `auth = "user"` (captura `$auth.id`)
- **Input:**
  - `student_id`: `int` (obrigatório)
  - `academic_task_id`: `int` (obrigatório)
  - `grade`: `decimal` (obrigatório, escala avaliativa)
  - `feedback`: `text?` (opcional)
- **Processamento:**
  - Validação dos parâmetros de entrada
  - Inserção na tabela `activity_grades` com `user_id: $auth.id`
  - Retorno do registro criado

## Risks / Trade-offs

- **[Risco] Integridade relacional com IDs inexistentes** → **Mitigação**: Validar a existência do aluno e da tarefa antes de persistir ou assegurar chaves estrangeiras ativas no banco.

