# Proposal

## Why

Atualmente, as telas de Disciplinas (`pages/1_📚_Disciplinas.py`) e Tarefas (`pages/2_📝_Tarefas.py`) exibem dados estáticos ou parciais e não realizam a sincronização completa com os dados do usuário autenticado no backend Xano. Com a autenticação já implementada na plataforma, é necessário integrar essas telas com as tabelas `subjects` e `academic_tasks` por meio dos endpoints REST do Xano, assegurando que cada usuário visualize e gerencie exclusivamente seus próprios registros.

## What Changes

- Criar o serviço reutilizável `services/task_service.py` com funções HTTP baseadas na biblioteca `requests` para listar, cadastrar e atualizar o status de tarefas na tabela `academic_tasks` do Xano.
- Atualizar o serviço `services/subject_service.py` para consumir a URL base definida no `.env` e integrar com autenticação do usuário via Bearer Token.
- Conectar a página `pages/1_📚_Disciplinas.py` aos endpoints da tabela `subjects` para cadastrar e listar disciplinas reais preservando o layout e abas existentes.
- Conectar a página `pages/2_📝_Tarefas.py` aos endpoints da tabela `academic_tasks` para listar, buscar por texto, filtrar por status e atualizar tarefas acadêmicas vinculadas às disciplinas cadastradas.
- Adicionar tratamento completo de erros de rede/conexão, respostas HTTP inesperadas e estados vazios com avisos amigáveis no Streamlit.

## Capabilities

### New Capabilities
- `academic-tasks`: Gerenciamento e sincronização de tarefas acadêmicas vinculadas a disciplinas e ao usuário autenticado via endpoints Xano.

### Modified Capabilities
- `subjects`: Atualização da integração da página `pages/1_📚_Disciplinas.py` para utilizar autenticação por token da sessão e sincronização dinâmica com o Xano.

## Impact

- **Frontend**:
  - `pages/1_📚_Disciplinas.py`: Integração com `services/subject_service.py`.
  - `pages/2_📝_Tarefas.py`: Integração com `services/task_service.py` e mapeamento de disciplinas.
- **Serviços HTTP**:
  - Criação de `services/task_service.py`.
  - Refatoração de `services/subject_service.py` para alinhamento com `.env` e tokens de sessão.
- **Dependências**: Utilização das bibliotecas padrão `requests` e `streamlit`.

