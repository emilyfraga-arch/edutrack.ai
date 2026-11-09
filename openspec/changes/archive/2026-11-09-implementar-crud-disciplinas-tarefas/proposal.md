# Proposal

## Why

As páginas de Disciplinas (`pages/1_📚_Disciplinas.py`) e Tarefas (`pages/2_📝_Tarefas.py`) necessitam de integração completa com o backend Xano para persistência e consulta real de dados acadêmicos vinculados ao usuário autenticado. Para viabilizar essa integração com segurança e confiabilidade, é necessário implementar o conjunto completo de endpoints CRUD (POST, GET, GET por ID, PATCH e DELETE) para as tabelas `subjects` e `academic_tasks` em XanoScript com validação rigorosa de autenticação JWT e isolamento multitenant via `$auth.id`, conectando os serviços Python (`subject_service.py` e `task_service.py`) e as telas Streamlit.

## What Changes

- **Backend (XanoScript)**:
  - Criação do grupo de APIs e endpoints CRUD para `subjects`:
    - `POST /subjects`: cadastrar disciplina associando automaticamente `user_id = $auth.id`.
    - `GET /subjects`: listar disciplinas pertencentes exclusivamente ao usuário autenticado (`user_id == $auth.id`).
    - `GET /subjects/{subjects_id}`: consultar os dados detalhados de uma disciplina específica do usuário autenticado.
    - `PATCH /subjects/{subjects_id}`: atualizar dados da disciplina garantindo que pertença ao usuário autenticado.
    - `DELETE /subjects/{subjects_id}`: remover a disciplina garantindo que pertença ao usuário autenticado.
  - Criação do grupo de APIs e endpoints CRUD para `academic_tasks`:
    - `POST /academic_tasks`: cadastrar tarefa associando automaticamente `user_id = $auth.id` e `subject_id` válido.
    - `GET /academic_tasks`: listar tarefas acadêmicas pertencentes exclusivamente ao usuário autenticado (`user_id == $auth.id`).
    - `GET /academic_tasks/{academic_tasks_id}`: consultar detalhes de uma tarefa específica do usuário autenticado.
    - `PATCH /academic_tasks/{academic_tasks_id}`: atualizar status ou dados da tarefa do usuário autenticado.
    - `DELETE /academic_tasks/{academic_tasks_id}`: remover tarefa garantindo que pertença ao usuário autenticado.
  - Configuração de segurança JWT (`auth = "user"`) e validação de permissão/propriedade (`precondition $record.user_id == $auth.id`) em todas as operações individuais.
- **Configuração de Ambiente**:
  - Configuração das variáveis `XANO_AUTH_BASE_URL` e `XANO_API_URL` no `.env` na raiz do projeto.
- **Camada de Serviços (Python)**:
  - Atualização de `services/subject_service.py` com funções para `get_subjects`, `get_subject_by_id`, `create_subject`, `update_subject` e `delete_subject` consumindo `XANO_API_URL` com Bearer Token.
  - Atualização de `services/task_service.py` com funções para `get_academic_tasks`, `get_academic_task_by_id`, `create_academic_task`, `update_academic_task`, `update_task_status` e `delete_academic_task` consumindo `XANO_API_URL` com Bearer Token.
- **Frontend Streamlit**:
  - Atualização de `pages/1_📚_Disciplinas.py` para listar, cadastrar e permitir remoção de disciplinas consumindo os dados reais do Xano.
  - Atualização de `pages/2_📝_Tarefas.py` para listar, cadastrar novas tarefas associadas a disciplinas e alternar status/remover tarefas consumindo os dados reais do Xano.
  - Tratamento robusto de erros HTTP, falhas de conectividade, ausência de dados e feedback amigável no Streamlit.

## Capabilities

### New Capabilities
- `academic-tasks`: Gerenciamento completo de tarefas acadêmicas através de endpoints CRUD (POST, GET, GET/id, PATCH, DELETE) com autenticação JWT e propriedade por `$auth.id == user_id`, integrado à interface Streamlit.

### Modified Capabilities
- `subjects`: Atualização dos requisitos de segurança dos endpoints CRUD (POST, GET, GET/id, PATCH, DELETE) com validação estrita de autenticação JWT e propriedade por `$auth.id == user_id`, além de integração na interface Streamlit.

## Impact

- **Endpoints Backend**:
  - Novos arquivos `.xs` em `api/subjects/` e `api/academic_tasks/`.
- **Serviços HTTP**:
  - `services/subject_service.py` e `services/task_service.py` atualizados para CRUD completo.
- **Variáveis de Ambiente**:
  - Arquivo `.env` configurado com `XANO_AUTH_BASE_URL` e `XANO_API_URL`.
- **Interface do Usuário**:
  - `pages/1_📚_Disciplinas.py` e `pages/2_📝_Tarefas.py` com integração completa a dados remotos.

