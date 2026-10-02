import streamlit as st

st.title("🎓 EduTrack AI")
st.header("📚 Minhas Disciplinas")

tab1, tab2 = st.tabs([
    "➕ Adicionar Nova Disciplina",
    "📚 Disciplinas Cadastradas"
])

with tab1:
    st.subheader("Cadastrar disciplina")

    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome da disciplina")
        professor = st.text_input("Professor")

    with col2:
        codigo = st.text_input("Código")
        semestre = st.text_input("Semestre")

    if st.button("Cadastrar disciplina"):
        if nome and professor and codigo and semestre:
            st.success(f"Disciplina '{nome}' cadastrada com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

with tab2:
    st.subheader("Disciplinas Cadastradas")

    with st.expander("📚 Português"):
        st.write("**Professor:** Carlos")
        st.write("**Código:** PORT123")
        st.write("**Semestre:** 2026/1")

    with st.expander("📐 Matemática"):
        st.write("**Professor:** Professor de Matemática")
        st.write("**Código:** MAT123")
        st.write("**Semestre:** 2026/1")