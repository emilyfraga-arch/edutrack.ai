import streamlit as st
from services.subject_service import get_subjects, create_subject, delete_subject

# Configuração da Página
st.set_page_config(page_title="EduTrack AI", page_icon="🎓", layout="wide")

# Título Principal
st.title("🎓 EduTrack AI")

# Sidebar (Menu Lateral)
st.sidebar.header("Menu de Navegação")
menu_option = st.sidebar.radio("Navegar", ["Dashboard", "Disciplinas", "Tarefas"])

# Busca as disciplinas cadastradas
active_subjects = get_subjects(status="active")

# Conteúdo Dinâmico
if menu_option == "Dashboard":
    st.write("Bem-vindo ao seu assistente acadêmico inteligente!")
    
    # Métricas Visuais Dinâmicas
    col1, col2 = st.columns(2)
    col1.metric("Disciplinas Ativas", str(len(active_subjects)))
    col2.metric("Tarefas Pendentes", "0")
    
    st.markdown("---")
    st.subheader("Disciplinas em Andamento")
    if active_subjects:
        cols = st.columns(min(len(active_subjects), 3))
        for idx, subj in enumerate(active_subjects):
            with cols[idx % len(cols)]:
                st.info(f"**{subj.get('name')}**\n\n📌 Código: {subj.get('code') or 'N/A'}\n\n👨‍🏫 Professor: {subj.get('professor') or 'N/A'}")
    else:
        st.write("Nenhuma disciplina ativa encontrada. Adicione uma no menu **Disciplinas**.")

elif menu_option == "Disciplinas":
    st.subheader("📚 Minhas Disciplinas")
    
    # Formulário para Adicionar Disciplina
    with st.expander("➕ Adicionar Nova Disciplina", expanded=False):
        with st.form("new_subject_form", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Nome da Disciplina *", placeholder="Ex: Cálculo I")
                code = st.text_input("Código da Disciplina", placeholder="Ex: MAT101")
            with col_b:
                professor = st.text_input("Professor(a)", placeholder="Ex: Dr. Silva")
                semester = st.text_input("Semestre / Período", placeholder="Ex: 2026.1")
            
            submitted = st.form_submit_button("Cadastrar Disciplina")
            if submitted:
                if not name.strip():
                    st.error("O nome da disciplina é obrigatório.")
                else:
                    new_subj = create_subject(name=name, code=code, professor=professor, semester=semester)
                    if new_subj:
                        st.success(f"Disciplina '{name}' cadastrada com sucesso!")
                        st.rerun()

    # Listagem de Disciplinas
    st.markdown("### Disciplinas Cadastradas")
    all_subjects = get_subjects(status=None)
    
    if all_subjects:
        for subj in all_subjects:
            with st.container():
                c1, c2, c3, c4 = st.columns([3, 2, 2, 1])
                with c1:
                    st.markdown(f"**{subj.get('name')}**")
                    if subj.get("code"):
                        st.caption(f"Código: {subj.get('code')}")
                with c2:
                    st.text(f"👨‍🏫 {subj.get('professor') or 'Não informado'}")
                with c3:
                    st.text(f"📅 {subj.get('semester') or 'N/A'}")
                with c4:
                    if st.button("🗑️", key=f"del_{subj.get('id')}", help="Excluir disciplina"):
                        delete_subject(subj.get("id"))
                        st.rerun()
                st.divider()
    else:
        st.info("Nenhuma disciplina cadastrada ainda. Utilize o formulário acima para começar.")

elif menu_option == "Tarefas":
    st.subheader("Gerenciamento de Tarefas")
    st.checkbox("Exemplo: Estudar Streamlit")
    st.checkbox("Exemplo: Estudar Streamlit")