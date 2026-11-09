# Design: Implementação Completa CRUD Disciplinas e Tarefas (Xano & Streamlit)

## Context

See `proposal.md` for motivation and background.

Atualmente, o projeto EduTrack AI possui autenticação com login e cadastro funcionando via JWT (`auth/login`, `auth/signup`, `auth/me`), e as páginas de frontend (`pages/1_📚_Disciplinas.py` e `pages/2_📝_Tarefas.py`) consom serviços HTTP em Python (`services/subject_service.py` e `services/task_service.py`).
Para viabilizar a persistência real dos dados, é necessário formalizar no repositório os arquivos de endpoint XanoScript (.xs) nas pastas `api/subjects/` e `api/academic_tasks/`, garantir o controle de acesso por `$auth.id` em todas as consultas e mutações, e atualizar os serviços e páginas Streamlit para integração ponta a ponta com as tabelas do Xano.

## Goals / Non-Goals

**Goals:**
- Criar a suíte completa de endpoints CRUD (POST, GET, GET por ID, PATCH, DELETE) para as tabelas `subjects` e `academic_tasks` em XanoScript.
- Garantir segurança multitenancy em 100% dos endpoints: autenticação JWT via `auth = "user"`, injeção forçada de `user_id = $auth.id` em cadastros, filtragem em listagens e verificação de propriedade (`precondition $record.user_id == $auth.id`) em operações por ID.
- Atualizar `services/subject_service.py` e `services/task_service.py` para suportar todas as operações CRUD com tratamento robusto de erros HTTP e timeouts.
- Configurar `.env` com a distinção limpa de `XANO_AUTH_BASE_URL` e `XANO_API_URL`.
- Atualizar as telas `pages/1_📚_Disciplinas.py` e `pages/2_📝_Tarefas.py` para listar, cadastrar, atualizar status e excluir registros mantendo o layout e as funcionalidades pré-existentes.

**Non-Goals:**
- Não realizar push ou deploy automático para o servidor Xano (conforme Regra Nº 2 de `AGENTS.md`).
- Não modificar o fluxo de login ou cadastro (`pages/3_👤_Perfil.py` e `services/auth_service.py`).
- Não criar tabelas duplicadas ou adicionar campos não relacionados ao escopo.

## Architecture & Technical Design

### 1. Estrutura do Banco de Dados Xano

#### Tabela `subjects`:
- `id` (int, auto-increment, PK)
- `user_id` (int, FK referencing `user.id`)
- `name` (text, obrigatório)
- `code` (text, opcional)
- `professor` (text, opcional)
- `semester` (text, opcional)
- `created_at` (timestamp, default `now`)

#### Tabela `academic_tasks`:
- `id` (int, auto-increment, PK)
- `user_id` (int, FK referencing `user.id`)
- `subject_id` (int, FK referencing `subjects.id`, opcional/associativo)
- `title` (text, obrigatório)
- `description` (text, opcional)
- `due_date` (text/date, opcional)
- `status` (text, default `"Pendente"`)
- `created_at` (timestamp, default `now`)

### 2. Endpoints XanoScript

#### Grupo de APIs `subjects` (`api/subjects/`):
- `api/subjects/api_group.xs`:
  ```xs
  api_group "subjects" {
    canonical = "subjects"
  }
  ```
- `POST /subjects` (`api/subjects/subjects_POST.xs`):
  - `auth = "user"`
  - Inputs: `name` (text), `code?` (text), `professor?` (text), `semester?` (text)
  - Stack: `db.add subjects` com `data = { user_id: $auth.id, name: $input.name, ... }`
- `GET /subjects` (`api/subjects/subjects_GET.xs`):
  - `auth = "user"`
  - Inputs: `status?` (text)
  - Stack: `db.query subjects` com `where = $db.subjects.user_id == $auth.id`
- `GET /subjects/{subjects_id}` (`api/subjects/subjects/subjects_id_GET.xs`):
  - `auth = "user"`
  - Stack: `db.get subjects`, `precondition ($subjects != null && $subjects.user_id == $auth.id)`
- `PATCH /subjects/{subjects_id}` (`api/subjects/subjects/subjects_id_PATCH.xs`):
  - `auth = "user"`
  - Stack: validação de propriedade, `db.patch subjects`
- `DELETE /subjects/{subjects_id}` (`api/subjects/subjects/subjects_id_DELETE.xs`):
  - `auth = "user"`
  - Stack: validação de propriedade, `db.del subjects`

#### Grupo de APIs `academic_tasks` (`api/academic_tasks/`):
- `api/academic_tasks/api_group.xs`:
  ```xs
  api_group "academic_tasks" {
    canonical = "academic_tasks"
  }
  ```
- `POST /academic_tasks` (`api/academic_tasks/academic_tasks_POST.xs`):
  - `auth = "user"`
  - Inputs: `title` (text), `description?` (text), `due_date?` (text), `status?` (text), `subject_id?` (int)
  - Stack: `db.add academic_tasks` com `data = { user_id: $auth.id, ... }`
- `GET /academic_tasks` (`api/academic_tasks/academic_tasks_GET.xs`):
  - `auth = "user"`
  - Inputs: `status?` (text), `subject_id?` (int)
  - Stack: `db.query academic_tasks` com `where = $db.academic_tasks.user_id == $auth.id`
- `GET /academic_tasks/{academic_tasks_id}` (`api/academic_tasks/academic_tasks/academic_tasks_id_GET.xs`):
  - `auth = "user"`
  - Stack: `db.get academic_tasks`, `precondition ($academic_tasks != null && $academic_tasks.user_id == $auth.id)`
- `PATCH /academic_tasks/{academic_tasks_id}` (`api/academic_tasks/academic_tasks/academic_tasks_id_PATCH.xs`):
  - `auth = "user"`
  - Stack: validação de propriedade, `db.patch academic_tasks`
- `DELETE /academic_tasks/{academic_tasks_id}` (`api/academic_tasks/academic_tasks/academic_tasks_id_DELETE.xs`):
  - `auth = "user"`
  - Stack: validação de propriedade, `db.del academic_tasks`

### 3. Integração com Serviços Streamlit

- **Configuração (`.env`)**:
  ```env
  XANO_AUTH_BASE_URL=https://x8ki-letl-twmt.n7.xano.io/api:50EO7Tkz
  XANO_API_URL=https://x8ki-letl-twmt.n7.xano.io/api:50EO7Tkz
  ```
- **`services/subject_service.py`**:
  - `get_subjects(token, status)` -> `GET {XANO_API_URL}/subjects`
  - `get_subject_by_id(subject_id, token)` -> `GET {XANO_API_URL}/subjects/{id}`
  - `create_subject(name, code, professor, semester, token)` -> `POST {XANO_API_URL}/subjects`
  - `update_subject(subject_id, data, token)` -> `PATCH {XANO_API_URL}/subjects/{id}`
  - `delete_subject(subject_id, token)` -> `DELETE {XANO_API_URL}/subjects/{id}`
- **`services/task_service.py`**:
  - `get_academic_tasks(token)` -> `GET {XANO_API_URL}/academic_tasks`
  - `get_academic_task_by_id(task_id, token)` -> `GET {XANO_API_URL}/academic_tasks/{id}`
  - `create_academic_task(title, description, due_date, status, subject_id, token)` -> `POST {XANO_API_URL}/academic_tasks`
  - `update_academic_task(task_id, data, token)` -> `PATCH {XANO_API_URL}/academic_tasks/{id}`
  - `update_task_status(task_id, status, token)` -> `PATCH {XANO_API_URL}/academic_tasks/{id}`
  - `delete_academic_task(task_id, token)` -> `DELETE {XANO_API_URL}/academic_tasks/{id}`

### 4. Interface Streamlit

- **`pages/1_📚_Disciplinas.py`**:
  - Aba 1 ("Adicionar Nova Disciplina"): formulário de cadastro conectado a `create_subject`.
  - Aba 2 ("Disciplinas Cadastradas"): lista de disciplinas do usuário; em cada expander, botões para remover disciplina com confirmação.
- **`pages/2_📝_Tarefas.py`**:
  - Seção superior com busca de texto e filtro de status ("Todas", "Pendente", "Concluída").
  - Expander/Seção de cadastro: "➕ Adicionar Nova Tarefa" com campos `title`, `description`, `due_date`, e `subject_id` (populado dinamicamente via `get_subjects`).
  - Lista de tarefas com checkbox de conclusão e botão de exclusão da tarefa.

## Decisions

- **Decisão 1: Endpoints isolados por recurso**: Criação de grupos e diretórios próprios `api/subjects/` e `api/academic_tasks/` em vez de reutilizar grupos genéricos de teste, facilitando modularidade e manutenção.
  *Alternativa descartada*: Adicionar dentro de `api/teste` ou `api/crud_apis_basico`. A estrutura modular isolada por recurso reflete boas práticas REST e a arquitetura do Xano.
- **Decisão 2: Validação de Propriedade do Registro**: Em todas as operações por ID (GET, PATCH, DELETE), o XanoScript verifica `precondition ($record != null && $record.user_id == $auth.id)`. Caso contrário, retorna 404 (evitando inclusive vazamento de existência de registro de outro usuário).
  *Alternativa descartada*: Confiar apenas no ID enviado. Isso causaria falha grave de segurança IDOR (Insecure Direct Object Reference).
- **Decisão 3: Reutilização de Token JWT**: Uso estrito do token `st.session_state["auth_token"]` obtido no login da Tarefa 14 em todas as chamadas HTTP via header `Authorization: Bearer <token>`.

## Risks / Trade-offs

- **[Risco: Tabelas ainda não migradas no ambiente remoto Xano]** → Mitigação: Criar e validar todos os arquivos `.xs` localmente e disponibilizar para o desenvolvedor realizar o push manual para o Xano. Tratar códigos de erro HTTP e mensagens amigáveis no Streamlit.
- **[Risco: Inconsistência de URL no .env]** → Mitigação: Suportar fallback de `XANO_API_URL` para `XANO_AUTH_BASE_URL` nas funções de serviço, assegurando funcionamento caso o usuário mantenha uma única URL base configurada.
- **[Risco: Remoção acidental de disciplinas com tarefas vinculadas]** → Mitigação: Na interface Streamlit, incluir confirmação visual antes de executar a deleção.

