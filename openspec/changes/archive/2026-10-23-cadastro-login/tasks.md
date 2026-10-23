# Tasks

## 1. Configuração de Ambiente

- [x] 1.1 Criar arquivo `.env` na raiz do projeto contendo a variável `XANO_AUTH_BASE_URL` para armazenar a URL base dos endpoints de autenticação do Xano

## 2. Implementação do Perfil e Autenticação (Streamlit)

- [x] 2.1 Implementar funções de requisição HTTP para os endpoints `auth/signup`, `auth/login` e `auth/me` utilizando a URL base configurada no `.env`
- [x] 2.2 Implementar formulários de Login (`auth/login`) e Cadastro (`auth/signup`) com persistência de token no `st.session_state` em `pages/3_👤_Perfil.py`
- [x] 2.3 Implementar tela de exibição dos dados do usuário autenticado via `auth/me` com botão de logout em `pages/3_👤_Perfil.py`

