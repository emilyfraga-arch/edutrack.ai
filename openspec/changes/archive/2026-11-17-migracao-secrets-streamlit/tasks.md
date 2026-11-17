# Tasks

## 1. Configuração de Secrets do Streamlit

- [x] 1.1 Configurar o arquivo `.streamlit/secrets.toml` com sintaxe TOML válida contendo `XANO_AUTH_BASE_URL` e `XANO_API_URL`

## 2. Migração da Leitura de URLs nos Serviços e Páginas

- [x] 2.1 Atualizar `services/auth_service.py` para priorizar o carregamento das URLs via `st.secrets` com fallback para variáveis de ambiente e `.env`
- [x] 2.2 Atualizar as mensagens informativas em `pages/3_👤_Perfil.py` referenciando `secrets.toml`

## 3. Validação e Testes

- [x] 3.1 Verificar a sintaxe dos arquivos Python modificados e testar a resolução de secrets
- [x] 3.2 Validar a especificação completa executando `openspec validate migracao-secrets-streamlit`
