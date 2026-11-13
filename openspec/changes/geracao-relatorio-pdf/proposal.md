# Proposal

## Why

Alunos e professores necessitam de um meio padronizado, exportável e profissional para consultar e compartilhar o histórico de desempenho acadêmico no EduTrack AI. A criação de um script em Python para geração de relatório em formato PDF, acompanhado de um endpoint dedicado no backend Xano para viabilizar o download desse arquivo com controle de autenticação, atende à necessidade de emissão de comprovantes de aproveitamento e acompanhamento acadêmico.

## What Changes

- **Backend XanoScript**:
  - Criação do grupo de APIs `reports` em `api/reports/api_group.xs`.
  - Criação do endpoint `GET /reports/student_performance_pdf` em `api/reports/student_performance_pdf_GET.xs`, protegido com `auth = "user"`, para recuperar os dados e metadados de download do relatório do aluno autenticado.
- **Script Python**:
  - Criação de `scripts/generate_student_report_pdf.py` para consultar os dados do aluno, disciplinas e tarefas acadêmicas, gerando um documento PDF formatado contendo cabeçalho institucional, indicadores de progresso, lista de disciplinas e tarefas com seus respectivos status.
  - Integração para disponibilizar o arquivo gerado para download via endpoint do Xano.

## Capabilities

### New Capabilities
- `student-report-pdf`: Geração de relatório de desempenho acadêmico em formato PDF e disponibilização de endpoint no Xano para download do relatório pelo aluno autenticado.

### Modified Capabilities
<!-- Nenhuma especificação permanente existente tem seus requisitos alterados nesta mudança. -->

## Impact

- **Novo diretório e endpoint XanoScript**: `api/reports/api_group.xs` e `api/reports/student_performance_pdf_GET.xs`.
- **Novo script Python**: `scripts/generate_student_report_pdf.py`.
- **Bibliotecas Python**: Utilização de biblioteca para criação de PDF (como `reportlab` ou `fpdf2`) e consumo das APIs via `requests`.
- **APIs**: Novo endpoint `GET /reports/student_performance_pdf` integrado à autenticação JWT do usuário.
