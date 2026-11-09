# Tasks

## 1. Endpoints XanoScript para a Tabela subjects

- [x] 1.1 Criar o grupo de APIs `subjects` em `api/subjects/api_group.xs` e verificar a sintaxe do arquivo
- [x] 1.2 Criar o endpoint `POST /subjects` em `api/subjects/subjects_POST.xs` para cadastrar disciplina com `auth = "user"` e `user_id = $auth.id`
- [x] 1.3 Criar o endpoint `GET /subjects` em `api/subjects/subjects_GET.xs` para listar disciplinas com filtro obrigatório `where = $db.subjects.user_id == $auth.id`
- [x] 1.4 Criar o endpoint `GET /subjects/{subjects_id}` em `api/subjects/subjects/subjects_id_GET.xs` para consultar disciplina específica validando propriedade do usuário autenticado
- [x] 1.5 Criar o endpoint `PATCH /subjects/{subjects_id}` em `api/subjects/subjects/subjects_id_PATCH.xs` para atualizar disciplina validando propriedade do usuário autenticado
- [x] 1.6 Criar o endpoint `DELETE /subjects/{subjects_id}` em `api/subjects/subjects/subjects_id_DELETE.xs` para excluir disciplina validando propriedade do usuário autenticado

## 2. Endpoints XanoScript para a Tabela academic_tasks

- [x] 2.1 Criar o grupo de APIs `academic_tasks` em `api/academic_tasks/api_group.xs` e verificar a sintaxe do arquivo
- [x] 2.2 Criar o endpoint `POST /academic_tasks` em `api/academic_tasks/academic_tasks_POST.xs` para cadastrar tarefa com `auth = "user"`, `user_id = $auth.id` e `subject_id`
- [x] 2.3 Criar o endpoint `GET /academic_tasks` em `api/academic_tasks/academic_tasks_GET.xs` para listar tarefas com filtro obrigatório `where = $db.academic_tasks.user_id == $auth.id`
- [x] 2.4 Criar o endpoint `GET /academic_tasks/{academic_tasks_id}` em `api/academic_tasks/academic_tasks/academic_tasks_id_GET.xs` para consultar tarefa específica validando propriedade do usuário autenticado
- [x] 2.5 Criar o endpoint `PATCH /academic_tasks/{academic_tasks_id}` em `api/academic_tasks/academic_tasks/academic_tasks_id_PATCH.xs` para atualizar dados ou status da tarefa validando propriedade do usuário autenticado
- [x] 2.6 Criar o endpoint `DELETE /academic_tasks/{academic_tasks_id}` em `api/academic_tasks/academic_tasks/academic_tasks_id_DELETE.xs` para excluir tarefa validando propriedade do usuário autenticado

## 3. Configuração de Ambiente e Serviços Python

- [x] 3.1 Configurar as variáveis `XANO_AUTH_BASE_URL` e `XANO_API_URL` no arquivo `.env` na raiz do projeto e validar leitura via `services/auth_service.py`
- [x] 3.2 Atualizar `services/subject_service.py` implementando funções para `get_subjects`, `get_subject_by_id`, `create_subject`, `update_subject` e `delete_subject` utilizando `requests` e Bearer Token
- [x] 3.3 Atualizar `services/task_service.py` implementando funções para `get_academic_tasks`, `get_academic_task_by_id`, `create_academic_task`, `update_academic_task`, `update_task_status` e `delete_academic_task` utilizando `requests` e Bearer Token

## 4. Integração das Páginas Streamlit

- [x] 4.1 Atualizar `pages/1_📚_Disciplinas.py` para listar e cadastrar disciplinas consumindo o Xano, incluindo controle de exclusão/atualização e tratamento de erros
- [x] 4.2 Atualizar `pages/2_📝_Tarefas.py` para listar, buscar, filtrar por status, cadastrar tarefas associadas a disciplinas e alternar status/excluir tarefas consumindo o Xano com tratamento de erros

## 5. Validação e Testes

- [x] 5.1 Verificar a sintaxe de todos os arquivos Python e XanoScript gerados
- [x] 5.2 Validar a especificação completa executando `openspec validate implementar-crud-disciplinas-tarefas`

