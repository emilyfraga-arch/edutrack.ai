# Proposal

## Why

Atualmente, o sistema EduTrack AI não possui um mecanismo estruturado para que os professores possam registrar avaliações e atribuir notas aos alunos em atividades acadêmicas específicas. A inclusão dessa funcionalidade viabiliza o lançamento oficial de notas, permitindo a consolidação do desempenho dos estudantes nas atividades avaliativas.

## What Changes

- Introduzir a capability `activity-grades` para gerenciar o lançamento de notas de atividades.
- Definir a estrutura de dados da tabela `activity_grades` vinculada ao professor (`user_id`), ao aluno (`student_id`) e à atividade avaliada (`academic_task_id`).
- Especificar o endpoint de API `POST /activity_grades` para permitir que o professor lance a nota da atividade para um estudante.

## Capabilities

### New Capabilities
- `activity-grades`: Permite que professores lancem notas para alunos em atividades acadêmicas específicas.

### Modified Capabilities
<!-- Nenhuma capability modificada -->

## Impact

- **Database**: Criação do esquema da tabela `activity_grades` em `tables/` pelo Xano Table Designer.
- **Backend API**: Criação do endpoint `POST /activity_grades` no grupo de API `apis/activity_grades/` pelo Xano API Query Writer.
- **Segurança**: Validação de autenticação do professor e vínculo obrigatório com `user_id`.

