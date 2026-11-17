# Design: Migração de Leitura de Variáveis de Ambiente para Streamlit Secrets

## Context

See `proposal.md` for motivation and background.

Atualmente, o projeto utiliza arquivos `.env` para armazenar `XANO_AUTH_BASE_URL` e `XANO_API_URL`. O ecossistema Streamlit oferece suporte nativo e seguro para credenciais através de `st.secrets` com o arquivo `.streamlit/secrets.toml`. O objetivo deste design é migrar a leitura primária de configurações para `st.secrets`, mantendo compatibilidade resiliente com scripts CLI e ambientes de teste.

## Goals / Non-Goals

**Goals:**
- Configurar `.streamlit/secrets.toml` com sintaxe TOML válida (valores entre aspas duplas).
- Atualizar a lógica de recuperação de URLs em `services/auth_service.py` (`get_base_url` e `get_api_url`) para priorizar `st.secrets`.
- Manter fallback em cascata para `os.getenv` e arquivo `.env` para preservar o funcionamento de scripts que rodam fora do Streamlit (como `scripts/calculate_progress.py` e `scripts/generate_student_report_pdf.py`).
- Atualizar avisos na interface (`pages/3_👤_Perfil.py`) informando sobre a configuração via `secrets.toml`.

**Non-Goals:**
- Não remover completamente o arquivo `.env` para não quebrar fluxos locais já existentes.
- Não alterar contratos de endpoints ou esquemas de dados no Xano.

## Decisions

- **Decisão 1: Hierarquia de Carregamento em Cascata (Fallback)**:
  *Ordem*: `st.secrets` → `os.getenv` → `.streamlit/secrets.toml` (leitura direta) → `.env`.
  *Motivação*: Garante que a aplicação Streamlit use primariamente a forma oficial recomendada (`st.secrets`), mas não quebra scripts CLI que são executados diretamente via terminal Python sem o runtime do Streamlit.
- **Decisão 2: Formatação estrita do `.streamlit/secrets.toml`**:
  *Motivação*: Chaves e valores formatados como `CHAVE = "VALOR"` respeitando a especificação TOML, evitando erros de parseamento da biblioteca `tomllib`/`toml`.

## Risks / Trade-offs

- **[Risco: `st.secrets` lançar exceção fora de contexto Streamlit]** → Mitigação: Proteger o acesso a `st.secrets` com bloco `try/except (AttributeError, FileNotFoundError, Exception)`.
- **[Risco: Inconsistência entre valores em `.env` e `secrets.toml`]** → Mitigação: Definir prioridade clara (`secrets.toml` prevalece sobre `.env`).
