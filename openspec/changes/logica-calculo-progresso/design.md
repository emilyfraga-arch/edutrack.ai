# Design: Cálculo de Progresso de Disciplinas Baseado em Tarefas

## Context

See `proposal.md` for motivation and background.

No EduTrack AI, as disciplinas (`subjects`) possuem tarefas acadêmicas associadas (`academic_tasks`), ambas gerenciadas via endpoints CRUD RESTful no Xano com isolamento por usuário autenticado. Para permitir que a plataforma e ferramentas externas calculem indicadores de desempenho do aluno, será desenvolvido um script em `scripts/calculate_progress.py` que calcula a taxa de conclusão de uma disciplina a partir de suas tarefas e entrega o resultado em formato JSON.

## Goals / Non-Goals

**Goals:**
- Implementar a função e script CLI `scripts/calculate_progress.py`.
- Consumir os endpoints CRUD existentes (`subjects` e `academic_tasks`) via `services.subject_service` e `services.task_service` (ou requisições HTTP autenticadas).
- Calcular de forma determinística: total de tarefas, tarefas concluídas, tarefas pendentes e porcentagem de progresso `(concluídas / total) * 100`.
- Retornar o resultado estritamente em formato JSON estruturado.
- Tratar de forma resiliente situações sem tarefas (evitar divisão por zero, retornando 0.0%), disciplina inexistente, erros de autenticação ou indisponibilidade de rede.

**Non-Goals:**
- Não criar novas tabelas ou novos endpoints no backend Xano.
- Não alterar as páginas do Streamlit nesta mudança específica (o script poderá ser importado futuramente por componentes de UI).
- Não executar deploy ou push para o Xano.

## Decisions

- **Decisão 1: Reutilização dos serviços CRUD existentes (`services/subject_service.py` e `services/task_service.py`)**:
  *Motivação*: Os serviços já encapsulam tratamento de URLs base (`XANO_API_URL` / `XANO_AUTH_BASE_URL`), cabeçalhos `Authorization: Bearer`, parâmetros de filtro e timeouts.
  *Alternativa considerada*: Escrever chamadas `requests` do zero dentro do script. Descartado para evitar código duplicado e inconsistências de configuração do `.env`.
- **Decisão 2: Critério de tarefa concluída padronizado**:
  *Motivação*: Tarefas podem ter valores de status textuais como "Concluída", "concluida", "completed" ou "done". O cálculo normalizará o texto (`.strip().lower()`) para aferir a conclusão de modo robusto.
  *Alternativa considerada*: Comparar estritamente com `status == "Concluída"`. Descartado por ser frágil a variações de capitalização.
- **Decisão 3: Formato JSON consistente para sucesso e falha**:
  *Motivação*: Em cenários de sucesso, o JSON retorna campos numéricos e descritivos. Em caso de falha (disciplina não encontrada, falha de token), retorna `{"subject_id": id, "error": msg}` com formatação válida para evitar quebra de consumidores.

## Risks / Trade-offs

- **[Risco: Disciplina sem nenhuma tarefa cadastrada]** → Mitigação: Verificação explícita de `total == 0` retornando `progress_percentage: 0.0`, prevenindo `ZeroDivisionError`.
- **[Risco: Execução sem token fornecido]** → Mitigação: O script suportará passagem via argumento CLI (`--token`), variável de ambiente ou leitura interativa, retornando mensagem de erro JSON clara se ausente.

