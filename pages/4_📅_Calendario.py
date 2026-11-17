import streamlit as st
import calendar
from datetime import date, datetime, timedelta
from styles.theme import apply_custom_theme, render_page_header

# Configuração da Página
st.set_page_config(page_title="Calendário - EduTrack AI", page_icon="📅", layout="wide")

# Aplica Tema Visual Padronizado
apply_custom_theme()

# Cabeçalho Padronizado
render_page_header(
    title="Calendário Acadêmico",
    subtitle="Visualize provas, entregas, seminários e datas importantes do seu semestre.",
    badge_text="Agenda & Prazos",
    icon="📅"
)

# Tipos de Eventos, Badges e Ícones
EVENT_TYPES = {
    "Prova": {
        "badge_class": "badge-red",
        "dot_color": "#EF4444",
        "emoji": "🔴",
        "icon": "📝",
        "label": "Prova / Exame",
    },
    "Trabalho": {
        "badge_class": "badge-purple",
        "dot_color": "#8B5CF6",
        "emoji": "🟣",
        "icon": "💻",
        "label": "Trabalho / Projeto",
    },
    "Entrega": {
        "badge_class": "badge-amber",
        "dot_color": "#F59E0B",
        "emoji": "🟡",
        "icon": "⏳",
        "label": "Entrega / Prazo",
    },
    "Aula Especial": {
        "badge_class": "badge-green",
        "dot_color": "#10B981",
        "emoji": "🟢",
        "icon": "🎓",
        "label": "Aula Especial / Seminário",
    },
}

# Inicialização de Estado do Calendário
today = date.today()

if "cal_year" not in st.session_state:
    st.session_state["cal_year"] = today.year
if "cal_month" not in st.session_state:
    st.session_state["cal_month"] = today.month
if "cal_selected_date" not in st.session_state:
    st.session_state["cal_selected_date"] = today

# Eventos Demonstrativos Iniciais (armazenados localmente)
if "calendar_events" not in st.session_state:
    st.session_state["calendar_events"] = [
        {
            "id": 1,
            "title": "Prova de Estruturas de Dados",
            "type": "Prova",
            "date": (today + timedelta(days=2)).strftime("%Y-%m-%d"),
            "time": "19:00 - 21:00",
            "location": "Sala 302 - Bloco B",
            "description": "Conteúdo: Árvores Binárias, Grafos e Algoritmos de Busca.",
        },
        {
            "id": 2,
            "title": "Entrega do Projeto de Banco de Dados",
            "type": "Entrega",
            "date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
            "time": "Até 23:59",
            "location": "Portal Acadêmico / GitHub",
            "description": "Envio do repositório com scripts SQL e documentação do modelo ER.",
        },
        {
            "id": 3,
            "title": "Apresentação: Inteligência Artificial",
            "type": "Trabalho",
            "date": (today + timedelta(days=9)).strftime("%Y-%m-%d"),
            "time": "14:30 - 16:00",
            "location": "Auditório Central",
            "description": "Apresentação em slides sobre redes neurais e processamento de linguagem natural.",
        },
        {
            "id": 4,
            "title": "Seminário de Metodologia e Ética",
            "type": "Aula Especial",
            "date": (today + timedelta(days=12)).strftime("%Y-%m-%d"),
            "time": "10:00 - 12:00",
            "location": "Online via Google Meet",
            "description": "Palestra com pesquisadores convidados sobre bioética e dados na ciência.",
        },
        {
            "id": 5,
            "title": "Avaliação Intermediária de Cálculo",
            "type": "Prova",
            "date": (today + timedelta(days=16)).strftime("%Y-%m-%d"),
            "time": "08:00 - 10:00",
            "location": "Sala 105 - Bloco A",
            "description": "Integrais duplas, equações diferenciais e aplicações geométricas.",
        },
        {
            "id": 6,
            "title": "Entrega de Relatório de Redes",
            "type": "Entrega",
            "date": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
            "time": "23:59",
            "location": "Ambiente Virtual",
            "description": "Relatório das práticas de roteamento e protocolo TCP/IP no laboratório.",
        },
    ]

# Variáveis Ativas de Navegação
cur_year = st.session_state["cal_year"]
cur_month = st.session_state["cal_month"]
selected_date_obj = st.session_state.get("cal_selected_date", today)

month_names_pt = [
    "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Barra Superior de Navegação
col_nav_prev, col_nav_title, col_nav_today, col_nav_next = st.columns([1, 4, 1.4, 1])

with col_nav_prev:
    if st.button("◀ Mês Ant.", use_container_width=True, key="btn_cal_prev"):
        if cur_month == 1:
            st.session_state["cal_month"] = 12
            st.session_state["cal_year"] -= 1
        else:
            st.session_state["cal_month"] -= 1
        st.rerun()

with col_nav_title:
    month_label = f"📅 {month_names_pt[cur_month]} de {cur_year}"
    st.markdown(
        f"<h2 style='text-align: center; margin: 0; padding: 4px 0; font-size: 1.45rem; color: #FFFFFF;'>{month_label}</h2>",
        unsafe_allow_html=True
    )

with col_nav_today:
    if st.button("Hoje 📌", use_container_width=True, key="btn_cal_today"):
        st.session_state["cal_year"] = today.year
        st.session_state["cal_month"] = today.month
        st.session_state["cal_selected_date"] = today
        st.rerun()

with col_nav_next:
    if st.button("Próx. Mês ▶", use_container_width=True, key="btn_cal_next"):
        if cur_month == 12:
            st.session_state["cal_month"] = 1
            st.session_state["cal_year"] += 1
        else:
            st.session_state["cal_month"] += 1
        st.rerun()

st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)

# Legenda Visual das Cores
st.markdown(
    """
    <div style="display: flex; gap: 10px; align-items: center; justify-content: center; flex-wrap: wrap; margin-bottom: 1.25rem;">
        <span class="edutrack-badge badge-red">🔴 Prova</span>
        <span class="edutrack-badge badge-purple">🟣 Trabalho</span>
        <span class="edutrack-badge badge-amber">🟡 Entrega</span>
        <span class="edutrack-badge badge-green">🟢 Aula Especial</span>
        <span style="font-size: 0.8rem; color: #60A5FA; font-weight: 600; padding: 2px 6px;">🔵 Borda Azul = Hoje</span>
        <span style="font-size: 0.8rem; color: #C4B5FD; font-weight: 600; padding: 2px 6px;">🟣 Fundo Roxo = Selecionado</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Mapeia eventos por data para consulta rápida
events_by_date = {}
for ev in st.session_state["calendar_events"]:
    d_str = ev.get("date")
    if d_str:
        if d_str not in events_by_date:
            events_by_date[d_str] = []
        events_by_date[d_str].append(ev)

# Monta matriz do mês (Domingo a Sábado)
calendar.setfirstweekday(calendar.SUNDAY)
month_cal = calendar.monthcalendar(cur_year, cur_month)
days_of_week = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

# CSS Específico para os Botões e Grade do Calendário
st.markdown(
    """
    <style>
    /* Estilo Uniforme para Células do Calendário */
    div[class*="st-key-cal_"] button {
        height: 52px !important;
        min-height: 52px !important;
        max-height: 52px !important;
        border-radius: 8px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        transition: all 0.2s ease-in-out !important;
        box-sizing: border-box !important;
    }

    /* Dias Normais */
    div[class*="st-key-cal_day_"] button {
        background-color: #161922 !important;
        border: 1px solid #282B37 !important;
        color: #F3F4F6 !important;
    }
    div[class*="st-key-cal_day_"] button:hover {
        border-color: #8B5CF6 !important;
        background-color: #1E222E !important;
        transform: translateY(-2px) !important;
    }

    /* Dia Atual (Hoje) - Destaque em Azul */
    div[class*="st-key-cal_today_"] button {
        background-color: rgba(59, 130, 246, 0.2) !important;
        border: 2px solid #3B82F6 !important;
        color: #93C5FD !important;
        font-weight: 700 !important;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.35) !important;
    }
    div[class*="st-key-cal_today_"] button:hover {
        background-color: rgba(59, 130, 246, 0.35) !important;
        border-color: #60A5FA !important;
        color: #FFFFFF !important;
    }

    /* Dia Selecionado - Destaque em Roxo */
    div[class*="st-key-cal_selected_"] button,
    div[class*="st-key-cal_today_selected_"] button {
        background-color: #8B5CF6 !important;
        border: 2px solid #7C3AED !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        box-shadow: 0 0 14px rgba(139, 92, 246, 0.5) !important;
    }
    div[class*="st-key-cal_selected_"] button:hover,
    div[class*="st-key-cal_today_selected_"] button:hover {
        background-color: #7C3AED !important;
        border-color: #6D28D9 !important;
    }

    /* Células Vazias (Fora do mês) */
    div[class*="st-key-cal_empty_"] button {
        background-color: transparent !important;
        border: 1px dashed #242836 !important;
        color: #4B5563 !important;
        cursor: default !important;
        box-shadow: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout Principal: Calendário (60%) e Eventos (40%)
col_cal_grid, col_cal_events = st.columns([1.8, 1.2], gap="large")

with col_cal_grid:
    st.markdown("### Visão Mensal")

    # Cabeçalho dos Dias da Semana (7 colunas perfeitamente alinhadas)
    header_cols = st.columns(7)
    for idx, dow in enumerate(days_of_week):
        header_cols[idx].markdown(
            f"<div style='text-align: center; font-weight: 700; font-size: 0.85rem; color: #C4B5FD; padding-bottom: 8px;'>{dow}</div>",
            unsafe_allow_html=True
        )

    # Grade de Semanas e Dias
    for week_idx, week in enumerate(month_cal):
        week_cols = st.columns(7)
        for col_idx, day_num in enumerate(week):
            with week_cols[col_idx]:
                if day_num == 0:
                    # Célula vazia fora do mês com altura uniforme
                    st.button(
                        "·",
                        key=f"cal_empty_{cur_year}_{cur_month}_{week_idx}_{col_idx}",
                        disabled=True,
                        use_container_width=True
                    )
                else:
                    day_date = date(cur_year, cur_month, day_num)
                    day_str = day_date.strftime("%Y-%m-%d")
                    day_events = events_by_date.get(day_str, [])

                    is_today = (day_date == today)
                    is_selected = (day_date == selected_date_obj)

                    # Monta pequenos indicadores visuais coloridos
                    indicators = ""
                    if day_events:
                        seen_types = set()
                        for ev in day_events:
                            ev_t = ev.get("type", "Trabalho")
                            if ev_t not in seen_types:
                                seen_types.add(ev_t)
                                ev_meta = EVENT_TYPES.get(ev_t, EVENT_TYPES["Trabalho"])
                                indicators += ev_meta["emoji"]
                                if len(indicators) >= 2:
                                    break

                    # Rótulo conciso e centralizado do botão
                    if indicators:
                        btn_label = f"{day_num} {indicators}"
                    else:
                        btn_label = str(day_num)

                    # Determina a chave CSS única para estilo
                    if is_today and is_selected:
                        btn_key = f"cal_today_selected_{cur_year}_{cur_month}_{day_num}"
                        btn_type = "primary"
                    elif is_selected:
                        btn_key = f"cal_selected_{cur_year}_{cur_month}_{day_num}"
                        btn_type = "primary"
                    elif is_today:
                        btn_key = f"cal_today_{cur_year}_{cur_month}_{day_num}"
                        btn_type = "secondary"
                    else:
                        btn_key = f"cal_day_{cur_year}_{cur_month}_{day_num}"
                        btn_type = "secondary"

                    # Botão da célula do dia
                    if st.button(btn_label, key=btn_key, type=btn_type, use_container_width=True):
                        st.session_state["cal_selected_date"] = day_date
                        st.rerun()

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # Formulário para Adicionar Evento Demonstrativo
    with st.expander("➕ Adicionar Evento Demonstrativo ao Calendário", expanded=False):
        with st.form("form_add_calendar_event", clear_on_submit=True):
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                ev_title = st.text_input("Título do Evento *", placeholder="Ex: Prova Final de Algoritmos")
                ev_type = st.selectbox("Categoria", list(EVENT_TYPES.keys()))
            with f_col2:
                ev_date = st.date_input("Data do Evento", value=selected_date_obj)
                ev_time = st.text_input("Horário / Prazo", placeholder="Ex: 14:00 - 16:00 ou Até 23:59")

            ev_desc = st.text_area("Descrição / Local (opcional)", placeholder="Ex: Sala 204 ou Link do Teams")
            ev_submit = st.form_submit_button("Salvar Evento no Calendário")

            if ev_submit:
                if not ev_title.strip():
                    st.error("Informe o título do evento.")
                else:
                    new_ev = {
                        "id": len(st.session_state["calendar_events"]) + 1,
                        "title": ev_title.strip(),
                        "type": ev_type,
                        "date": ev_date.strftime("%Y-%m-%d"),
                        "time": ev_time.strip() or "Dia todo",
                        "location": ev_desc.strip() or "Não especificado",
                        "description": ev_desc.strip(),
                    }
                    st.session_state["calendar_events"].append(new_ev)
                    st.session_state["cal_selected_date"] = ev_date
                    st.session_state["cal_year"] = ev_date.year
                    st.session_state["cal_month"] = ev_date.month
                    st.success(f"Evento '{ev_title}' adicionado ao calendário com sucesso!")
                    st.rerun()

with col_cal_events:
    # Mostra eventos da data selecionada
    sel_date_str = selected_date_obj.strftime("%Y-%m-%d")
    sel_events = events_by_date.get(sel_date_str, [])

    st.markdown(f"### Eventos em {selected_date_obj.strftime('%d/%m/%Y')}")

    if sel_events:
        for ev in sel_events:
            ev_meta = EVENT_TYPES.get(ev.get("type", "Trabalho"), EVENT_TYPES["Trabalho"])
            st.markdown(
                f"""
                <div class="event-item-card" style="border-left: 4px solid {ev_meta['dot_color']};">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span class="edutrack-badge {ev_meta['badge_class']}">{ev_meta['icon']} {ev.get('type')}</span>
                        <span style="font-size: 0.8rem; color: #9CA3AF;">🕒 {ev.get('time', 'Dia todo')}</span>
                    </div>
                    <div style="font-weight: 700; color: #FFFFFF; font-size: 1.05rem; margin-bottom: 4px;">{ev.get('title')}</div>
                    <div style="font-size: 0.85rem; color: #D1D5DB; margin-bottom: 4px;">📍 {ev.get('location', 'Geral')}</div>
                    <div style="font-size: 0.82rem; color: #9CA3AF;">{ev.get('description', '')}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info(f"Nenhum evento registrado para o dia {selected_date_obj.strftime('%d/%m/%Y')}.")

    st.markdown("---")

    # Lista Geral de Próximos Eventos
    st.markdown("### 🔔 Próximos Eventos")

    filtro_tipo = st.selectbox(
        "Filtrar por Categoria",
        ["Todas"] + list(EVENT_TYPES.keys()),
        key="select_filtro_proximos_eventos"
    )

    # Ordena eventos por data crescente
    sorted_events = sorted(
        st.session_state["calendar_events"],
        key=lambda x: x.get("date", "")
    )

    filtered_events = []
    for ev in sorted_events:
        if filtro_tipo != "Todas" and ev.get("type") != filtro_tipo:
            continue
        filtered_events.append(ev)

    if not filtered_events:
        st.caption("Nenhum evento corresponde ao filtro selecionado.")
    else:
        for ev in filtered_events[:6]:
            ev_meta = EVENT_TYPES.get(ev.get("type", "Trabalho"), EVENT_TYPES["Trabalho"])
            try:
                ev_d_parsed = datetime.strptime(ev.get("date"), "%Y-%m-%d").strftime("%d/%m")
            except Exception:
                ev_d_parsed = ev.get("date")

            st.markdown(
                f"""
                <div class="event-item-card" style="border-left: 3px solid {ev_meta['dot_color']}; padding: 10px 12px; margin-bottom: 8px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span class="edutrack-badge {ev_meta['badge_class']}">{ev_meta['icon']} {ev.get('type')}</span>
                        <span style="font-size: 0.82rem; font-weight: 600; color: #C4B5FD;">📅 {ev_d_parsed}</span>
                    </div>
                    <div style="font-weight: 600; color: #FFFFFF; font-size: 0.95rem; margin-top: 6px;">{ev.get('title')}</div>
                    <div style="font-size: 0.8rem; color: #9CA3AF; margin-top: 2px;">🕒 {ev.get('time', 'Dia todo')}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
