import streamlit as st
from services.auth_service import login, signup, get_me, get_base_url

# Configuração da Página
st.set_page_config(page_title="Perfil - EduTrack AI", page_icon="👤", layout="wide")

st.title("👤 Perfil do Usuário")

# Verifica se a URL base do Xano está configurada
base_url = get_base_url()
if not base_url:
    st.warning("⚠️ **Aviso de Configuração:** A variável `XANO_AUTH_BASE_URL` não foi definida no arquivo `.env`.")

# Inicialização de estado da sessão
if "auth_token" not in st.session_state:
    st.session_state["auth_token"] = None
if "user_profile" not in st.session_state:
    st.session_state["user_profile"] = None

# Fluxo 1: Usuário Autenticado
if st.session_state["auth_token"]:
    success, profile_data = get_me(st.session_state["auth_token"])
    
    if success:
        st.session_state["user_profile"] = profile_data
        st.success(f"Bem-vindo(a), **{profile_data.get('name', 'Estudante')}**!")
        
        st.markdown("### Informações da Conta")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Nome:** {profile_data.get('name', 'N/A')}\n\n**Email:** {profile_data.get('email', 'N/A')}")
        with col2:
            st.info(f"**Identificador (ID):** {profile_data.get('id', 'N/A')}\n\n**Perfil/Função:** {profile_data.get('role', 'member')}")
        
        st.markdown("---")
        if st.button("🚪 Sair da Conta (Logout)", type="secondary"):
            st.session_state["auth_token"] = None
            st.session_state["user_profile"] = None
            st.success("Sessão finalizada com sucesso.")
            st.rerun()
    else:
        st.error("Sua sessão expirou ou o token de autenticação é inválido. Por favor, faça login novamente.")
        st.session_state["auth_token"] = None
        st.session_state["user_profile"] = None
        if st.button("Voltar para tela de login"):
            st.rerun()

# Fluxo 2: Usuário Não Autenticado (Login e Cadastro)
else:
    st.write("Acesse sua conta ou realize seu cadastro para gerenciar suas atividades acadêmicas.")
    
    tab_login, tab_signup = st.tabs(["🔐 Entrar (Login)", "📝 Criar Conta (Cadastro)"])
    
    with tab_login:
        st.subheader("Login na Plataforma")
        with st.form("form_login", clear_on_submit=False):
            login_email = st.text_input("Email", placeholder="exemplo@edutrack.ai", key="login_email")
            login_password = st.text_input("Senha", type="password", key="login_password")
            btn_login = st.form_submit_button("Entrar", use_container_width=True)
            
            if btn_login:
                if not login_email.strip() or not login_password:
                    st.error("Por favor, preencha o email e a senha.")
                else:
                    with st.spinner("Autenticando..."):
                        success, resp = login(email=login_email, password=login_password)
                        if success:
                            token = resp.get("authToken")
                            st.session_state["auth_token"] = token
                            st.session_state["user_id"] = resp.get("user_id")
                            st.success("Login realizado com sucesso!")
                            st.rerun()
                        else:
                            st.error(resp.get("message", "Falha na autenticação."))
                            
    with tab_signup:
        st.subheader("Cadastrar Novo Usuário")
        with st.form("form_signup", clear_on_submit=True):
            signup_name = st.text_input("Nome Completo", placeholder="Seu Nome Completo", key="signup_name")
            signup_email = st.text_input("Email", placeholder="seu.email@exemplo.com", key="signup_email")
            signup_password = st.text_input("Senha (mínimo 8 caracteres)", type="password", key="signup_password")
            signup_password_confirm = st.text_input("Confirmar Senha", type="password", key="signup_password_confirm")
            btn_signup = st.form_submit_button("Cadastrar", use_container_width=True)
            
            if btn_signup:
                if not signup_name.strip() or not signup_email.strip() or not signup_password:
                    st.error("Por favor, preencha todos os campos obrigatórios.")
                elif signup_password != signup_password_confirm:
                    st.error("As senhas informadas não coincidem.")
                elif len(signup_password) < 8:
                    st.error("A senha deve ter no mínimo 8 caracteres.")
                else:
                    with st.spinner("Criando conta..."):
                        success, resp = signup(name=signup_name, email=signup_email, password=signup_password)
                        if success:
                            token = resp.get("authToken")
                            st.session_state["auth_token"] = token
                            st.session_state["user_id"] = resp.get("user_id")
                            st.success("Conta criada e autenticada com sucesso!")
                            st.rerun()
                        else:
                            st.error(resp.get("message", "Falha ao realizar cadastro."))

