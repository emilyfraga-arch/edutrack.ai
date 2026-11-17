# Design: Geração de Relatório de Desempenho em PDF e Endpoint no Xano

## Context

See `proposal.md` for motivation and background.

No EduTrack AI, as informações acadêmicas do aluno estão distribuídas entre as tabelas `user`, `subjects` e `academic_tasks` no backend Xano. Para fornecer uma visão consolidada e exportável do desempenho do estudante, é necessária uma solução composta por um endpoint no Xano que agrega os dados acadêmicos do usuário autenticado e um script Python especializado que transforma esses dados em um documento PDF formatado e profissional.

## Goals / Non-Goals

**Goals:**
- Criar o grupo de APIs `reports` e o endpoint `GET /reports/student_performance_pdf` em XanoScript (`.xs`), protegido por autenticação JWT (`auth = "user"`), garantindo que apenas dados pertencentes ao usuário logado (`$auth.id`) sejam retornados.
- Implementar o script Python `scripts/generate_student_report_pdf.py` para gerar o relatório PDF contendo identificação do aluno, resumo quantitativo de progresso e detalhamento de disciplinas e tarefas acadêmicas.
- Fornecer suporte a execução CLI do script com opção de salvar o PDF gerado localmente em disco.
- Integrar o fluxo de consumo com autenticação via Bearer token e configuração no `.env`.

**Non-Goals:**
- Não realizar deploy ou push automático para o ambiente Xano (conforme Regra Nº 2 de `AGENTS.md`).
- Não alterar as telas existentes do Streamlit nesta etapa inicial (a integração visual pode ser proposta em mudança subsequente).
- Não criar tabelas adicionais no banco de dados.

## Decisions

- **Decisão 1: Criação do grupo de APIs `reports` em `api/reports/`**:
  *Motivação*: Agrupa endpoints relacionados a relatórios e exportações de dados, mantendo a arquitetura modular já estabelecida em `api/subjects/` e `api/academic_tasks/`.
  *Alternativa considerada*: Incluir em `api/crud_edutrack_ai/`. Descartado por se tratar de agregação analítica e não de operações CRUD genéricas.
- **Decisão 2: Agregação segura no XanoScript com `auth = "user"`**:
  *Motivação*: O endpoint no Xano busca os dados de `user`, `subjects` e `academic_tasks` aplicando estritamente o filtro `$auth.id`, impedindo que qualquer usuário consulte o desempenho de outro.
- **Decisão 3: Biblioteca de geração de PDF em Python**:
  *Motivação*: Uso de `reportlab` (ou `fpdf2`), padrões amplamente adotados na comunidade Python para geração programática e estilizada de documentos PDF vetoriais com tabelas, cabeçalhos e controle de quebra de página.
  *Alternativa considerada*: Exportar em HTML e converter via navegador headless. Descartado devido à sobrecarga de dependências externas.

## Risks / Trade-offs

- **[Risco: Aluno sem disciplinas cadastradas ao gerar o relatório]** → Mitigação: O script tratará coleções vazias exibindo mensagens claras como "Nenhuma disciplina cadastrada" no PDF, sem interromper a geração.
- **[Risco: Dependência de biblioteca PDF no ambiente Python]** → Mitigação: Adicionar a biblioteca necessária (`reportlab`) ao `requirements.txt` / ambiente virtual e validar com testes automatizados.
