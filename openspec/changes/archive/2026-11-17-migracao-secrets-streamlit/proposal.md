# Proposal

## Why

Atualmente, as URLs base das APIs do Xano (`XANO_AUTH_BASE_URL` e `XANO_API_URL`) são lidas diretamente do arquivo `.env`. No ecossistema Streamlit, a prática recomendada e padrão para gerenciar credenciais e configurações sensíveis de forma segura é através de `st.secrets` (`.streamlit/secrets.toml`). A migração da leitura dessas variáveis para os segredos do Streamlit melhora a segurança, padroniza a gestão de configurações da aplicação e facilita o deploy na nuvem (Streamlit Community Cloud).

## What Changes

- Correção e padronização da sintaxe do arquivo [`.streamlit/secrets.toml`](file:///c:/Users/2601914/Desktop/edutrack.ai/.streamlit/secrets.toml) para formato TOML válido com valores entre aspas.
- Atualização das funções `get_base_url()` e `get_api_url()` em [`services/auth_service.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/services/auth_service.py) para priorizar a leitura via `st.secrets`, mantendo fallback resiliente para variáveis de ambiente e `.env` (garantindo compatibilidade com scripts CLI).
- Atualização das mensagens e avisos em [`pages/3_👤_Perfil.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/pages/3_👤_Perfil.py) para indicar a configuração via Streamlit secrets (`secrets.toml`).

## Capabilities

### New Capabilities
<!-- Nenhuma nova capacidade é introduzida. -->

### Modified Capabilities
- `auth-profile`: Atualização do requisito de carregamento das URLs base para priorizar `st.secrets` (`.streamlit/secrets.toml`) com suporte a fallback de ambiente.

## Impact

- **Configuração**: Criação/ajuste de `.streamlit/secrets.toml` com sintaxe TOML válida.
- **Serviços**: [`services/auth_service.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/services/auth_service.py).
- **Frontend**: [`pages/3_👤_Perfil.py`](file:///c:/Users/2601914/Desktop/edutrack.ai/pages/3_👤_Perfil.py).
