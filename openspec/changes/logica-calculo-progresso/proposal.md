# Proposal

## Why

Para acompanhar o desempenho acadêmico e visualização de métricas no EduTrack AI, é necessário calcular automaticamente o percentual de conclusão das disciplinas com base nas tarefas acadêmicas registradas no Xano. A criação de um script utilitário dedicado permitirá obter esses dados de forma estruturada em formato JSON, consumindo os endpoints CRUD existentes e servindo de base para dashboards e indicadores do aluno.

## What Changes

- Criação do script Python `scripts/calculate_progress.py`.
- Implementação de função que recebe o identificador de uma disciplina (`subject_id`) e token de autenticação, consome os endpoints CRUD do Xano para buscar os dados da disciplina e suas tarefas associadas.
- Cálculo da porcentagem de progresso da disciplina com base na fórmula `(concluídas / total) * 100`, tratando o caso limite de 0 tarefas com `0.0%`.
- Retorno dos dados consolidados em formato JSON padronizado com os campos: `subject_id`, `subject_name`, `total_tasks`, `completed_tasks`, `pending_tasks` e `progress_percentage`.
- Suporte a execução via linha de comando (CLI) exibindo a saída em JSON formatado.

## Capabilities

### New Capabilities
- `progress-calculation`: Cálculo e consolidação de métricas de progresso de disciplinas baseadas no status de suas tarefas acadêmicas via endpoints CRUD, com retorno estruturado em JSON.

### Modified Capabilities
<!-- Nenhuma especificação permanente existente tem seus requisitos alterados nesta mudança. -->

## Impact

- **Novo arquivo**: `scripts/calculate_progress.py`.
- **Dependências consumidas**: `services/subject_service.py`, `services/task_service.py` (ou chamadas diretas via endpoints CRUD com `requests`), e biblioteca padrão `json`.
- **APIs**: Consumo dos endpoints CRUD `GET /subjects/{id}` e `GET /academic_tasks` do Xano.

