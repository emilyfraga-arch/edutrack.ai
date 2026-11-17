import streamlit as st
from services.auth_service import login, signup, get_me, get_base_url
from styles.theme import (
    apply_custom_theme,
    render_page_header,
    get_active_accent,
    get_active_avatar,
    sync_local_storage,
    AVATARS,
    ACCENT_PALETTES,
)

# Configuração da Página
st.set_page_config(page_title="Perfil - EduTrack AI", page_icon="👤", layout="wide")

# Aplica Tema Visual Padronizado
apply_custom_theme()

# Cabeçalho Padronizado
render_page_header(
    title="Perfil do Usuário",
    subtitle="Gerencie suas credenciais de acesso, informações cadastrais e preferências visuais.",
    badge_text="Conta & Acesso",
    icon="👤"
)

# Verifica se a URL base do Xano está configurada
base_url = get_base_url()
if not base_url:
    st.warning("⚠️ **Aviso de Configuração:** A variável `XANO_AUTH_BASE_URL` não foi configurada em `.streamlit/secrets.toml` ou no ambiente.")

# Inicialização de estado da sessão de autenticação
if "auth_token" not in st.session_state:
    st.session_state["auth_token"] = None
if "user_profile" not in st.session_state:
    st.session_state["user_profile"] = None

# Inicialização de preferências visuais locais
if "user_avatar_id" not in st.session_state:
    st.session_state["user_avatar_id"] = "student"
if "user_accent_choice" not in st.session_state:
    st.session_state["user_accent_choice"] = "Roxo EduTrack (Padrão)"
if "user_theme_mode" not in st.session_state:
    st.session_state["user_theme_mode"] = "Escuro (Padrão EduTrack)"

active_avatar = get_active_avatar()
active_accent = get_active_accent()

def render_preferences_section():
    """Renderiza a seção de personalização visual com persistência local no navegador."""
    st.markdown("### 🎨 Preferências Visuais e Personalização")
    st.caption("Personalize sua experiência visual no EduTrack AI. As configurações são salvas localmente no seu navegador.")

    with st.container():
        st.markdown("<div class='edutrack-card'>", unsafe_allow_html=True)
        col_p1, col_p2 = st.columns(2)

        with col_p1:
            st.markdown("#### 1. Escolha seu Avatar")
            avatar_labels = [f"{av['icon']} {av['label']}" for av in AVATARS]
            current_av_idx = 0
            for idx, av in enumerate(AVATARS):
                if av["id"] == st.session_state["user_avatar_id"]:
                    current_av_idx = idx
                    break

            selected_av_label = st.selectbox(
                "Avatar do Perfil",
                avatar_labels,
                index=current_av_idx,
                key="select_user_avatar"
            )
            # Mapeia de volta para o objeto de avatar
            chosen_av_obj = AVATARS[avatar_labels.index(selected_av_label)]

            st.markdown(
                f"""
                <div style="display: flex; align-items: center; gap: 12px; margin-top: 10px; padding: 10px; background-color: #1A1D27; border-radius: 8px; border: 1px solid #282B37;">
                    <div style="font-size: 2rem; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; background: {active_accent['rgba']}; border-radius: 50%;">
                        {chosen_av_obj['icon']}
                    </div>
                    <div>
                        <div style="font-weight: 600; color: #FFFFFF; font-size: 0.95rem;">{chosen_av_obj['label']}</div>
                        <div style="font-size: 0.78rem; color: #9CA3AF;">Avatar ativo para seu perfil</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_p2:
            st.markdown("#### 2. Cor de Destaque do Sistema")
            palette_names = list(ACCENT_PALETTES.keys())
            cur_palette_idx = palette_names.index(st.session_state["user_accent_choice"]) if st.session_state["user_accent_choice"] in palette_names else 0

            selected_accent_name = st.selectbox(
                "Paleta de Cores",
                palette_names,
                index=cur_palette_idx,
                key="select_user_accent"
            )
            preview_accent = ACCENT_PALETTES[selected_accent_name]

            st.markdown(
                f"""
                <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px; padding: 10px; background-color: #1A1D27; border-radius: 8px; border: 1px solid #282B37;">
                    <div style="width: 32px; height: 32px; border-radius: 6px; background-color: {preview_accent['hex']}; box-shadow: 0 0 10px {preview_accent['glow']};"></div>
                    <div>
                        <div style="font-weight: 600; color: #FFFFFF; font-size: 0.95rem;">{selected_accent_name}</div>
                        <div style="font-size: 0.78rem; color: #9CA3AF;">HEX: {preview_accent['hex']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        col_t1, col_t2 = st.columns(2)

        with col_t1:
            st.markdown("#### 3. Modo de Exibição (Tema)")
            theme_modes = ["Escuro (Padrão EduTrack)", "Claro Minimalista"]
            cur_theme_idx = theme_modes.index(st.session_state["user_theme_mode"]) if st.session_state["user_theme_mode"] in theme_modes else 0

            selected_theme_mode = st.radio(
                "Tema da Interface",
                theme_modes,
                index=cur_theme_idx,
                key="radio_user_theme_mode",
                horizontal=True
            )

        with col_t2:
            st.markdown("#### 4. Armazenamento Local")
            st.markdown(
                """
                <p style="font-size: 0.85rem; color: #9CA3AF; margin-top: 6px;">
                    Suas preferências são gravadas com segurança no <code>localStorage</code> do seu navegador, sem alterar o banco de dados.
                </p>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

        # Botão para Salvar Personalizações
        if st.button("💾 Salvar Personalizações", key="btn_save_customizations"):
            st.session_state["user_avatar_id"] = chosen_av_obj["id"]
            st.session_state["user_accent_choice"] = selected_accent_name
            st.session_state["user_theme_mode"] = selected_theme_mode

            # Sincroniza com o localStorage do navegador
            sync_local_storage({
                "avatar_id": chosen_av_obj["id"],
                "accent_choice": selected_accent_name,
                "theme_mode": selected_theme_mode,
            })

            st.success("✨ Personalizações salvas com sucesso no seu navegador!")
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# Fluxo 1: Usuário Autenticado
if st.session_state["auth_token"]:
    success, profile_data = get_me(st.session_state["auth_token"])

    if success:
        st.session_state["user_profile"] = profile_data
        user_name = profile_data.get('name', 'Estudante')
        user_email = profile_data.get('email', 'N/A')
        user_id = profile_data.get('id', 'N/A')
        user_role = profile_data.get('role', 'member')

        # Card de Resumo do Perfil com Avatar Personalizado
        st.markdown(
            f"""
            <div class="edutrack-card" style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 16px;">
                    <div style="width: 58px; height: 58px; border-radius: 50%; background: linear-gradient(135deg, {active_accent['hex']} 0%, {active_accent['hover']} 100%); display: flex; align-items: center; justify-content: center; font-size: 1.85rem; color: #FFFFFF; box-shadow: 0 4px 14px {active_accent['glow']};">
                        {active_avatar['icon']}
                    </div>
                    <div>
                        <div style="font-size: 1.3rem; font-weight: 700; color: #FFFFFF;">{user_name}</div>
                        <div style="display: flex; gap: 8px; align-items: center; margin-top: 4px; flex-wrap: wrap;">
                            <span class="edutrack-badge badge-green">✓ Sessão Ativa</span>
                            <span class="edutrack-badge badge-purple">{user_role.capitalize()}</span>
                            <span class="edutrack-badge badge-gray">{active_avatar['label']}</span>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Informações da Conta")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div class="edutrack-meta-box">
                    <div class="edutrack-meta-label">👤 Nome Completo</div>
                    <div class="edutrack-meta-value">{user_name}</div>
                </div>
                <div class="edutrack-meta-box">
                    <div class="edutrack-meta-label">✉️ Email Cadastrado</div>
                    <div class="edutrack-meta-value">{user_email}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <div class="edutrack-meta-box">
                    <div class="edutrack-meta-label">🆔 Identificador no Sistema (ID)</div>
                    <div class="edutrack-meta-value">#{user_id}</div>
                </div>
                <div class="edutrack-meta-box">
                    <div class="edutrack-meta-label">🛡️ Perfil / Nível de Acesso</div>
                    <div class="edutrack-meta-value">{user_role.capitalize()}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        # Seção de Personalização Visual
        render_preferences_section()

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

# Fluxo 2: Usuário Não Autenticado (Login, Cadastro e Personalização)
else:
    st.caption("Acesse sua conta ou realize seu cadastro para sincronizar suas atividades acadêmicas.")

    tab_login, tab_signup, tab_custom = st.tabs([
        "🔐 Entrar (Login)",
        "📝 Criar Conta (Cadastro)",
        "🎨 Personalizar Interface"
    ])

    with tab_login:
        st.markdown("### Login na Plataforma")
        st.caption("Insira suas credenciais cadastradas para acessar.")
        with st.form("form_login", clear_on_submit=False):
            login_email = st.text_input("Email", placeholder="exemplo@edutrack.ai", key="login_email")
            login_password = st.text_input("Senha", type="password", key="login_password")
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
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
        st.markdown("### Cadastrar Novo Usuário")
        st.caption("Crie sua conta para começar a gerenciar disciplinas e tarefas.")
        with st.form("form_signup", clear_on_submit=True):
            signup_name = st.text_input("Nome Completo", placeholder="Seu Nome Completo", key="signup_name")
            signup_email = st.text_input("Email", placeholder="seu.email@exemplo.com", key="signup_email")
            signup_password = st.text_input("Senha (mínimo 8 caracteres)", type="password", key="signup_password")
            signup_password_confirm = st.text_input("Confirmar Senha", type="password", key="signup_password_confirm")
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
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

    with tab_custom:
        render_preferences_section()
