# Design

## Context

O EduTrack AI é um aplicativo Streamlit multipágina (`pages/1_📚_Disciplinas.py`, `pages/2_📝_Tarefas.py`, `pages/3_👤_Perfil.py`). A página de perfil atualmente encontra-se vazia.

No backend Xano, o grupo de autenticação já possui os seguintes endpoints definidos em `api/authentication/auth/`:
- `POST auth/signup` (recebe `name`, `email`, `password`, cria registro na tabela `user` e retorna `{authToken, user_id}`)
- `POST auth/login` (recebe `email`, `password`, valida credenciais e retorna `{authToken, user_id}`)
- `GET auth/me` (requer `auth = "user"` com Bearer token e retorna dados do usuário: `id`, `name`, `email`, `role`, etc.)

## Goals / Non-Goals

**Goals:**
- Configurar o arquivo `.env` na raiz do projeto com a variável `XANO_AUTH_BASE_URL` para centralizar a URL dos endpoints de autenticação.
- Implementar em `pages/3_👤_Perfil.py` o formulário de Login e o formulário de Cadastro de novos usuários.
- Salvar o token JWT retornado em `st.session_state.auth_token`.
- Realizar a chamada para `auth/me` passando o cabeçalho `Authorization: Bearer <token>` para renderizar os dados do usuário autenticado e disponibilizar ação de Logout.

**Non-Goals:**
- Fluxo de recuperação de senha via email/token externo (não solicitado).
- Autenticação social de terceiros (Google, Apple, etc.).
- Alterações nos endpoints do Xano (os endpoints existentes já cobrem a necessidade).

## Decisions

### 1. Configuração de Ambiente (.env)
- **Arquivo**: `.env` na raiz do repositório.
- **Variáveis**:
  - `XANO_AUTH_BASE_URL`: URL base para os endpoints de autenticação (ex.: `https://x8ki-letl-twmt.n7.xano.io/api:pbAs170Z` ou URL do workspace).
- **Biblioteca**: `python-dotenv` para carregamento seguro das variáveis de ambiente.

### 2. Gestão de Estado de Sessão (Streamlit Session State)
- Chaves utilizadas:
  - `st.session_state["auth_token"]`: Armazena a string do token JWT enquanto a sessão estiver ativa.
  - `st.session_state["user_profile"]`: Dicionário contendo os dados obtidos via `auth/me`.

### 3. Estrutura da Página `pages/3_👤_Perfil.py`
- **Se não autenticado (`auth_token` ausente)**:
  - Exibir abas (Tabs): **Login** e **Criar Conta**.
  - **Aba Login**: Campos `Email` e `Senha`, botão "Entrar". Dispara chamada para `POST auth/login`.
  - **Aba Criar Conta**: Campos `Nome Completo`, `Email`, `Senha` e `Confirmação de Senha`, botão "Cadastrar". Dispara chamada para `POST auth/signup`.
- **Se autenticado (`auth_token` presente)**:
  - Consulta `GET auth/me` e exibe cartão com: Nome, Email, Papel/Role e ID de Usuário.
  - Botão "Sair da Conta" (Logout) que remove o token da sessão e atualiza a interface via `st.rerun()`.

## Risks / Trade-offs

- **[Risco: Token inválido ou expirado]** → **Mitigação**: Caso o `GET auth/me` retorne status `401 Unauthorized`, limpar a chave `auth_token` da sessão e solicitar novo login do usuário.
- **[Risco: URL do Xano não configurada no .env]** → **Mitigação**: Exibir aviso amigável via `st.warning` orientando a configuração da variável `XANO_AUTH_BASE_URL`.

