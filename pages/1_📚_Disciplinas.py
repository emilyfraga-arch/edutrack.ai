import streamlit as st
from services.subject_service import get_subjects, create_subject, delete_subject
from styles.theme import apply_custom_theme, render_page_header

# Configuração da Página
st.set_page_config(page_title="Disciplinas - EduTrack AI", page_icon="📚", layout="wide")

# Aplica Tema Visual Padronizado
apply_custom_theme()

# Cabeçalho Padronizado
render_page_header(
    title="Minhas Disciplinas",
    subtitle="Gerencie o catálogo de matérias, códigos e professores do seu semestre acadêmico.",
    badge_text="Gestão Acadêmica",
    icon="📚"
)

# Recupera o token de autenticação da sessão
auth_token = st.session_state.get("auth_token")

if not auth_token:
    st.warning("⚠️ Você não está autenticado. Acesse a página **Perfil** para realizar login ou cadastro e sincronizar seus dados.")

tab1, tab2 = st.tabs([
    "➕ Adicionar Nova Disciplina",
    "📚 Disciplinas Cadastradas"
])

with tab1:
    st.markdown("### Cadastrar Nova Disciplina")
    st.caption("Preencha as informações da matéria para vinculação com suas tarefas.")

    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome da disciplina *", placeholder="Ex: Algoritmos e Estruturas de Dados", key="input_nome_disciplina")
        professor = st.text_input("Professor(a) *", placeholder="Ex: Dr. Alan Turing", key="input_prof_disciplina")

    with col2:
        codigo = st.text_input("Código da disciplina *", placeholder="Ex: CC-101", key="input_cod_disciplina")
        semestre = st.text_input("Semestre letivo *", placeholder="Ex: 2026.1", key="input_semestre_disciplina")

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    if st.button("Cadastrar disciplina", key="btn_cadastrar_disciplina"):
        if not auth_token:
            st.error("Você precisa estar logado para cadastrar disciplinas no Xano. Faça login na página de Perfil.")
        elif nome and professor and codigo and semestre:
            with st.spinner("Salvando disciplina no Xano..."):
                success, result = create_subject(
                    name=nome,
                    code=codigo,
                    professor=professor,
                    semester=semestre,
                    token=auth_token
                )
                if success:
                    st.success(f"Disciplina '{nome}' cadastrada com sucesso no Xano!")
                    st.rerun()
                else:
                    st.error(f"Erro ao salvar disciplina: {result}")
        else:
            st.warning("Preencha todos os campos obrigatórios.")

with tab2:
    st.markdown("### Disciplinas Cadastradas")

    if not auth_token:
        st.info("Faça login na página de Perfil para visualizar suas disciplinas salvas no Xano.")
    else:
        with st.spinner("Carregando disciplinas do Xano..."):
            success, result = get_subjects(token=auth_token)

        if not success:
            st.error(f"Erro ao buscar disciplinas: {result}")
        elif not result:
            st.info("Nenhuma disciplina cadastrada até o momento. Utilize a aba ao lado para adicionar.")
        else:
            for subj in result:
                sub_id = subj.get("id")
                sub_name = subj.get("name") or "Disciplina sem nome"
                prof = subj.get("professor") or subj.get("teacher") or "Não informado"
                cod = subj.get("code") or "Não informado"
                sem = subj.get("semester") or "Não informado"

                with st.expander(f"📚 {sub_name}"):
                    c_info, c_action = st.columns([3, 1])
                    with c_info:
                        st.markdown(
                            f"""
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-bottom: 8px;">
                                <div class="edutrack-meta-box">
                                    <div class="edutrack-meta-label">👨‍🏫 Professor</div>
                                    <div class="edutrack-meta-value">{prof}</div>
                                </div>
                                <div class="edutrack-meta-box">
                                    <div class="edutrack-meta-label">🏷️ Código</div>
                                    <div class="edutrack-meta-value">{cod}</div>
                                </div>
                                <div class="edutrack-meta-box">
                                    <div class="edutrack-meta-label">📅 Semestre</div>
                                    <div class="edutrack-meta-value">{sem}</div>
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_action:
                        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
                        if sub_id and st.button("🗑️ Excluir", key=f"btn_del_subj_{sub_id}"):
                            with st.spinner("Excluindo disciplina do Xano..."):
                                del_ok, del_res = delete_subject(sub_id, token=auth_token)
                                if del_ok:
                                    st.success("Disciplina removida com sucesso!")
                                    st.rerun()
                                else:
                                    st.error(f"Erro ao excluir: {del_res}")
