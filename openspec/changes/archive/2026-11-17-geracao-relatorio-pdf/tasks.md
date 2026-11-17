# Tasks

## 1. Endpoint no Xano para Relatório de Desempenho

- [x] 1.1 Criar o grupo de APIs `reports` em `api/reports/api_group.xs` e verificar sua sintaxe
- [x] 1.2 Criar o endpoint `GET /reports/student_performance_pdf` em `api/reports/student_performance_pdf_GET.xs` com `auth = "user"` e filtro estrito por `$auth.id`

## 2. Script Python de Geração de PDF

- [x] 2.1 Criar o script `scripts/generate_student_report_pdf.py` para consultar os dados do aluno, disciplinas e tarefas acadêmicas
- [x] 2.2 Implementar a renderização do arquivo PDF formatado contendo dados do aluno, métricas de progresso e listagem detalhada de disciplinas e tarefas
- [x] 2.3 Implementar a interface CLI no script para permitir gerar e salvar o relatório PDF localmente

## 3. Validação e Testes

- [x] 3.1 Verificar a sintaxe de todos os arquivos Python e XanoScript gerados
- [x] 3.2 Validar a especificação completa executando `openspec validate geracao-relatorio-pdf`
