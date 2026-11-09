# Tasks

## 1. Camada de Serviços HTTP (Requests)

- [x] 1.1 Atualizar `services/subject_service.py` com funções reutilizáveis para consultar e criar disciplinas no endpoint `/subjects` do Xano utilizando a URL base do `.env`, autenticação por token e tratamento de erros.
- [x] 1.2 Implementar `services/task_service.py` com funções reutilizáveis para consultar, cadastrar e atualizar tarefas no endpoint `/academic_tasks` do Xano utilizando a URL base do `.env`, autenticação por token e tratamento de erros.

## 2. Integração das Telas Streamlit

- [x] 2.1 Atualizar `pages/1_📚_Disciplinas.py` para sincronizar a listagem e cadastro com o backend Xano utilizando a autenticação da sessão, preservando o layout e abas existentes.
- [x] 2.2 Atualizar `pages/2_📝_Tarefas.py` para sincronizar a listagem, busca, filtro e status de tarefas com o backend Xano utilizando a autenticação da sessão, preservando o layout existente.

