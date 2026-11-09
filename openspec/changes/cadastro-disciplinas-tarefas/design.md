# Design

## Context

O EduTrack AI possui páginas dedicadas no Streamlit para navegação:
- `pages/1_📚_Disciplinas.py`: Tela de disciplinas com abas para cadastrar e listar disciplinas.
- `pages/2_📝_Tarefas.py`: Tela de tarefas acadêmicas com filtros por status e busca.
- `pages/3_👤_Perfil.py`: Gerenciamento de login e cadastro (onde `st.session_state["auth_token"]` é armazenado).

No backend Xano, as tabelas `subjects` e `academic_tasks` foram projetadas para armazenar respectivamente as disciplinas e tarefas acadêmicas dos alunos, exigindo o `user_id` do usuário autenticado via Bearer Token.

## Goals / Non-Goals

**Goals:**
- Centralizar o consumo da URL base a partir da função compartilhada `get_base_url()` baseada no arquivo `.env`.
- Criar a camada de serviço `services/task_service.py` para comunicação com os endpoints `/academic_tasks` do Xano via biblioteca `requests`.
- Refatorar `services/subject_service.py` para padronizar o envio de cabeçalhos de autenticação (`Authorization: Bearer <token>`) e leitura da URL base.
- Integrar a página `pages/1_📚_Disciplinas.py` para listar e cadastrar disciplinas reais do usuário no Xano.
- Integrar a página `pages/2_📝_Tarefas.py` para listar, buscar e atualizar status de tarefas reais do usuário vinculadas às suas disciplinas.
- Tratar falhas de conexão, ausência de dados e estado de autenticação preservando todo o layout visual do Streamlit.

**Non-Goals:**
- Criação de novos endpoints no backend Xano ou alteração nos esquemas de banco (endpoints já existentes da Tarefa 12 e Tarefa 11).
- Alteração no fluxo de login/signup implementado na Tarefa 14.

## Decisions

### 1. Camada de Comunicação HTTP (`services/`)
- **`services/subject_service.py`**:
  - `get_subjects(token: Optional[str])`: Faz chamada `GET /subjects` com header `Authorization: Bearer {token}`.
  - `create_subject(name, code, professor, semester, token: Optional[str])`: Faz chamada `POST /subjects` com payload `{name, code, professor, semester}` e token.
- **`services/task_service.py`**:
  - `get_academic_tasks(token: Optional[str])`: Faz chamada `GET /academic_tasks` com token e retorna lista de tarefas.
  - `create_academic_task(title, description, due_date, status, subject_id, token: Optional[str])`: Faz chamada `POST /academic_tasks`.
  - `update_task_status(task_id: int, status: str, token: Optional[str])`: Faz chamada `PATCH /academic_tasks/{task_id}` atualizando o status.
- Funções reutilizáveis tratando `requests.exceptions.RequestException`, retornando tuplas `(sucesso, dados_ou_mensagem)`.

### 2. Integração da Tela de Disciplinas (`pages/1_📚_Disciplinas.py`)
- Verificar se `st.session_state.get("auth_token")` existe. Se ausente, emitir aviso com `st.warning` e orientar login no Perfil.
- Na aba "➕ Adicionar Nova Disciplina":
  - Ao submeter o formulário com campos preenchidos, acionar `create_subject(...)`.
  - Exibir mensagem de sucesso ou erro e recarregar a interface com `st.rerun()`.
- Na aba "📚 Disciplinas Cadastradas":
  - Buscar disciplinas do usuário via `get_subjects(...)`.
  - Se vazia, exibir `st.info("Nenhuma disciplina cadastrada ainda.")`.
  - Para cada disciplina retornada, renderizar um expander com nome, código, professor e semestre.

### 3. Integração da Tela de Tarefas (`pages/2_📝_Tarefas.py`)
- Verificar `st.session_state.get("auth_token")`. Se ausente, emitir aviso com `st.warning`.
- Carregar mapa de disciplinas `{id: name}` via `get_subjects(token)` para exibir o nome da disciplina em cada tarefa.
- Carregar tarefas via `get_academic_tasks(token)`.
- Aplicar filtros na interface:
  - Busca textual pelo campo `search` no título ou descrição da tarefa.
  - Filtro por status (`filtro` selectbox: "Todas", "Pendente", "Concluída").
- Renderizar cada tarefa em um `st.expander` contendo título, disciplina associada, prazo (`due_date`) e checkbox de conclusão que chama `update_task_status(...)`.

## Risks / Trade-offs

- **[Risco: Usuário acessar as telas sem estar logado]**  
  → **Mitigação**: Exibir aviso claro na interface orientando a fazer login na página `pages/3_👤_Perfil.py` e desabilitar ações de escrita sem token.
- **[Risco: Instabilidade de conexão ou Xano offline]**  
  → **Mitigação**: Capturar exceções de conexão com `try/except` e exibir alertas visuais informativos com `st.error` sem quebrar a execução do Streamlit.

