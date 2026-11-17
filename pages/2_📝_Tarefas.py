import streamlit as st
from services.task_service import get_academic_tasks, create_academic_task, update_task_status, delete_academic_task
from services.subject_service import get_subjects
from styles.theme import apply_custom_theme, render_page_header

# Configuração da Página
st.set_page_config(page_title="Tarefas - EduTrack AI", page_icon="📝", layout="wide")

# Aplica Tema Visual Padronizado
apply_custom_theme()

# Cabeçalho Padronizado
render_page_header(
    title="Minhas Tarefas",
    subtitle="Organize, acompanhe e controle suas entregas e compromissos acadêmicos.",
    badge_text="Produtividade",
    icon="📝"
)

# Recupera o token de autenticação da sessão
auth_token = st.session_state.get("auth_token")

if not auth_token:
    st.warning("⚠️ Você não está autenticado. Acesse a página **Perfil** para realizar login ou cadastro e sincronizar suas tarefas.")

# Barra de Filtros e Busca
col1, col2 = st.columns([3, 1])

with col1:
    search = st.text_input("Buscar tarefa...", placeholder="Ex: Estudar Banco de Dados ou Projeto Final", key="input_search_tarefas")

with col2:
    filtro = st.selectbox("Status", ["Todas", "Pendente", "Concluída"], key="select_filtro_tarefas")

st.markdown("---")

if not auth_token:
    st.info("Faça login na página de Perfil para visualizar e gerenciar suas tarefas no Xano.")
else:
    # Busca disciplinas para mapear nomes associados a subject_id
    subject_map = {}
    subject_options = [("Nenhuma", None)]
    subj_success, subj_data = get_subjects(token=auth_token)
    if subj_success and isinstance(subj_data, list):
        for s in subj_data:
            s_id = s.get("id")
            s_name = s.get("name", f"Disciplina {s_id}")
            if s_id:
                subject_map[s_id] = s_name
                subject_options.append((s_name, s_id))

    # Formulário para cadastrar nova tarefa
    with st.expander("➕ Adicionar Nova Tarefa", expanded=False):
        with st.form("form_nova_tarefa", clear_on_submit=True):
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                nova_titulo = st.text_input("Título da Tarefa *", placeholder="Ex: Entregar relatório de Sistemas Operacionais")
                disciplina_idx = st.selectbox(
                    "Disciplina associada",
                    range(len(subject_options)),
                    format_func=lambda i: subject_options[i][0]
                )
            with f_col2:
                novo_prazo = st.text_input("Data de Entrega / Prazo", placeholder="Ex: 2026-11-20")
                nova_descricao = st.text_area("Descrição (opcional)", placeholder="Detalhes, requisitos ou instruções...")

            st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Cadastrar Tarefa")
            if submitted:
                if not nova_titulo.strip():
                    st.error("O título da tarefa é obrigatório.")
                else:
                    sel_subj_id = subject_options[disciplina_idx][1]
                    with st.spinner("Salvando tarefa no Xano..."):
                        cad_ok, cad_res = create_academic_task(
                            title=nova_titulo.strip(),
                            description=nova_descricao.strip(),
                            due_date=novo_prazo.strip(),
                            status="Pendente",
                            subject_id=sel_subj_id,
                            token=auth_token
                        )
                        if cad_ok:
                            st.success("Tarefa cadastrada com sucesso!")
                            st.rerun()
                        else:
                            st.error(f"Erro ao salvar tarefa: {cad_res}")

    # Busca as tarefas acadêmicas do usuário no Xano
    with st.spinner("Carregando tarefas do Xano..."):
        task_success, task_data = get_academic_tasks(token=auth_token)

    if not task_success:
        st.error(f"Erro ao buscar tarefas do Xano: {task_data}")
    elif not task_data:
        st.info("Nenhuma tarefa acadêmica encontrada no momento.")
    else:
        # Filtragem no cliente
        filtered_tasks = []
        for task in task_data:
            title = str(task.get("title") or "")
            desc = str(task.get("description") or "")
            status = str(task.get("status") or "Pendente")

            # Filtro por busca de texto
            if search and (search.lower() not in title.lower() and search.lower() not in desc.lower()):
                continue

            # Filtro por status
            is_completed = status.lower() in ["concluída", "concluida", "completed", "done"]
            if filtro == "Pendente" and is_completed:
                continue
            if filtro == "Concluída" and not is_completed:
                continue

            filtered_tasks.append(task)

        if not filtered_tasks:
            st.info("Nenhuma tarefa corresponde aos filtros aplicados.")
        else:
            for task in filtered_tasks:
                task_id = task.get("id")
                task_title = task.get("title") or "Sem título"
                task_desc = task.get("description")
                due_date = task.get("due_date") or "Não informado"
                status = task.get("status") or "Pendente"
                subj_id = task.get("subject_id")
                subj_name = subject_map.get(subj_id, "Não associada") if subj_id else "Não associada"

                is_done = str(status).lower() in ["concluída", "concluida", "completed", "done"]
                status_badge_html = (
                    '<span class="edutrack-badge badge-green">✓ Concluída</span>'
                    if is_done
                    else '<span class="edutrack-badge badge-amber">⏳ Pendente</span>'
                )

                with st.expander(f"📌 {task_title}", expanded=True):
                    c_det, c_del = st.columns([4, 1])
                    with c_det:
                        st.markdown(
                            f"""
                            <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 10px; flex-wrap: wrap;">
                                {status_badge_html}
                                <span class="edutrack-badge badge-purple">🏷️ {subj_name}</span>
                                <span class="edutrack-badge badge-gray">📅 Prazo: {due_date}</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        if task_desc:
                            st.markdown(
                                f"""
                                <div style="color: #D1D5DB; font-size: 0.92rem; margin-bottom: 12px; background-color: #1A1D27; padding: 10px 14px; border-radius: 8px; border: 1px solid #282B37;">
                                    {task_desc}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        # Checkbox para alternar status da tarefa
                        check_val = st.checkbox(
                            "Marcar como Concluída",
                            value=is_done,
                            key=f"task_check_{task_id}"
                        )

                        # Verifica se o estado mudou
                        if check_val != is_done:
                            new_status = "Concluída" if check_val else "Pendente"
                            with st.spinner("Atualizando tarefa no Xano..."):
                                up_ok, up_msg = update_task_status(task_id, new_status, token=auth_token)
                                if up_ok:
                                    st.success(f"Status atualizado para '{new_status}'!")
                                    st.rerun()
                                else:
                                    st.error(f"Erro ao atualizar status: {up_msg}")

                    with c_del:
                        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
                        if task_id and st.button("🗑️ Excluir", key=f"btn_del_task_{task_id}"):
                            with st.spinner("Excluindo tarefa do Xano..."):
                                d_ok, d_msg = delete_academic_task(task_id, token=auth_token)
                                if d_ok:
                                    st.success("Tarefa excluída com sucesso!")
                                    st.rerun()
                                else:
                                    st.error(f"Erro ao excluir tarefa: {d_msg}")
