# Proposal

## Why

Atualmente, o aplicativo EduTrack AI possui a página `pages/3_👤_Perfil.py` vazia e não dispõe de um fluxo de autenticação para os usuários. A implementação do cadastro e login permitirá que alunos e professores acessem a plataforma de forma segura e autenticada, persistindo suas credenciais na tabela `user` e consumindo os endpoints já existentes no Xano (`auth/login`, `auth/signup` e `auth/me`).

## What Changes

- Configurar arquivo `.env` na raiz do projeto para armazenar a URL base dos endpoints de autenticação do Xano.
- Implementar em `pages/3_👤_Perfil.py` as interfaces de login e cadastro de usuários via Streamlit.
- Integrar a página aos endpoints de autenticação:
  - `POST auth/signup`: Registro de novo usuário na tabela `user`.
  - `POST auth/login`: Autenticação e obtenção do token JWT.
  - `GET auth/me`: Consulta dos dados cadastrais do usuário autenticado.
- Gerenciar o estado de autenticação e o token de sessão utilizando `st.session_state`.

## Capabilities

### New Capabilities
- `auth-profile`: Fluxo de cadastro, autenticação e visualização do perfil do usuário na interface Streamlit integrado aos endpoints Xano.

### Modified Capabilities
<!-- Nenhuma capability modificada -->

## Impact

- **Frontend**: Criação da lógica de autenticação e interface visual em `pages/3_👤_Perfil.py`.
- **Configuração**: Novo arquivo `.env` na raiz do projeto armazenando a URL base da API.
- **Sessão**: Persistência do token de autenticação e dados do usuário no `st.session_state` do Streamlit.
- **Dependências**: Utilização de `python-dotenv` e `requests` para comunicação HTTP com o backend.

