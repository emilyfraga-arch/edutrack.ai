"""
Módulo de Estilização Centralizada - EduTrack AI
Define a identidade visual moderna em tema escuro com destaques em roxo e lilás,
com suporte a personalização dinâmica de cores, temas e componentes acadêmicos.
"""
import streamlit as st
import json

ACCENT_PALETTES = {
    "Roxo EduTrack (Padrão)": {
        "hex": "#8B5CF6",
        "hover": "#7C3AED",
        "light": "#C4B5FD",
        "rgba": "rgba(139, 92, 246, 0.18)",
        "glow": "rgba(139, 92, 246, 0.4)",
    },
    "Azul Elétrico": {
        "hex": "#3B82F6",
        "hover": "#2563EB",
        "light": "#93C5FD",
        "rgba": "rgba(59, 130, 246, 0.18)",
        "glow": "rgba(59, 130, 246, 0.4)",
    },
    "Verde Esmeralda": {
        "hex": "#10B981",
        "hover": "#059669",
        "light": "#6EE7B7",
        "rgba": "rgba(16, 185, 129, 0.18)",
        "glow": "rgba(16, 185, 129, 0.4)",
    },
    "Rosa Magenta": {
        "hex": "#EC4899",
        "hover": "#DB2777",
        "light": "#F472B6",
        "rgba": "rgba(236, 72, 153, 0.18)",
        "glow": "rgba(236, 72, 153, 0.4)",
    },
    "Âmbar Dourado": {
        "hex": "#F59E0B",
        "hover": "#D97706",
        "light": "#FCD34D",
        "rgba": "rgba(245, 158, 11, 0.18)",
        "glow": "rgba(245, 158, 11, 0.4)",
    },
    "Ciano Neon": {
        "hex": "#06B6D4",
        "hover": "#0891B2",
        "light": "#67E8F9",
        "rgba": "rgba(6, 182, 212, 0.18)",
        "glow": "rgba(6, 182, 212, 0.4)",
    },
}

AVATARS = [
    {"id": "student", "label": "Estudante Acadêmico", "icon": "🎓"},
    {"id": "developer", "label": "Desenvolvedor Tech", "icon": "👨‍💻"},
    {"id": "rocket", "label": "Inovador Espacial", "icon": "🚀"},
    {"id": "wizard", "label": "Mestre dos Estudos", "icon": "🧙‍♂️"},
    {"id": "owl", "label": "Coruja da Sabedoria", "icon": "🦉"},
    {"id": "fox", "label": "Raposa Estratégica", "icon": "🦊"},
    {"id": "ninja", "label": "Foco Total Ninja", "icon": "⚡"},
    {"id": "robot", "label": "Assistente IA", "icon": "🤖"},
]

def get_active_accent():
    """Retorna os dados da cor de destaque ativa da sessão."""
    chosen_label = st.session_state.get("user_accent_choice", "Roxo EduTrack (Padrão)")
    return ACCENT_PALETTES.get(chosen_label, ACCENT_PALETTES["Roxo EduTrack (Padrão)"])

def get_active_avatar():
    """Retorna o avatar ativo da sessão."""
    chosen_id = st.session_state.get("user_avatar_id", "student")
    for av in AVATARS:
        if av["id"] == chosen_id:
            return av
    return AVATARS[0]

def sync_local_storage(preferences: dict):
    """Injeta JavaScript para salvar preferências no localStorage do navegador."""
    json_data = json.dumps(preferences)
    st.components.v1.html(
        f"""
        <script>
        try {{
            window.parent.localStorage.setItem('edutrack_preferences', '{json_data}');
            console.log('EduTrack AI: Preferências salvas no localStorage.');
        }} catch(e) {{
            console.error('Erro ao salvar no localStorage:', e);
        }}
        </script>
        """,
        height=0,
        width=0
    )

def apply_custom_theme():
    """Injeta estilos CSS personalizados respeitando a identidade visual do EduTrack AI."""
    accent = get_active_accent()
    theme_mode = st.session_state.get("user_theme_mode", "Escuro (Padrão EduTrack)")

    # Configuração de modo claro vs escuro mantendo o menu lateral #262731
    if theme_mode == "Claro Minimalista":
        bg_main = "#F8FAFC"
        bg_card = "#FFFFFF"
        text_title = "#0F172A"
        text_body = "#334155"
        text_muted = "#64748B"
        border_card = "#E2E8F0"
        border_subtle = "#CBD5E1"
        input_bg = "#F1F5F9"
    else:
        bg_main = "#0E1015"
        bg_card = "#161922"
        text_title = "#FFFFFF"
        text_body = "#E5E7EB"
        text_muted = "#9CA3AF"
        border_card = "#282B37"
        border_subtle = "#242735"
        input_bg = "#161922"

    acc_hex = accent["hex"]
    acc_hover = accent["hover"]
    acc_light = accent["light"]
    acc_rgba = accent["rgba"]
    acc_glow = accent["glow"]

    st.markdown(
        f"""
        <style>
        /* =========================================================
           1. FUNDO PRINCIPAL E TIPOGRAFIA GERAL
           ========================================================= */
        .stApp, [data-testid="stAppViewContainer"] {{
            background-color: {bg_main} !important;
            color: {text_body} !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        }}

        /* Container principal */
        [data-testid="stMain"] .block-container {{
            padding-top: 2rem !important;
            padding-bottom: 3.5rem !important;
            max-width: 1080px !important;
        }}

        /* Títulos */
        h1 {{
            color: {text_title} !important;
            font-size: 1.95rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.025em !important;
            margin-bottom: 0.5rem !important;
        }}

        h2, h3 {{
            color: {text_title} !important;
            font-weight: 600 !important;
            letter-spacing: -0.015em !important;
        }}

        p, span, label {{
            color: {text_body} !important;
        }}

        /* Divisores */
        hr {{
            border: none !important;
            height: 1px !important;
            background-color: {border_subtle} !important;
            margin: 1.5rem 0 !important;
        }}

        /* =========================================================
           2. MENU LATERAL FIXO (SIDEBAR)
           ========================================================= */
        section[data-testid="stSidebar"] {{
            background-color: #262731 !important;
            border-right: 1px solid #333644 !important;
        }}

        section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
            background-color: #262731 !important;
            padding: 1.5rem 1rem !important;
        }}

        /* Itens de navegação na Sidebar */
        [data-testid="stSidebarNav"] {{
            padding-top: 0.5rem !important;
        }}

        [data-testid="stSidebarNav"] a {{
            border-radius: 8px !important;
            padding: 10px 14px !important;
            margin-bottom: 6px !important;
            transition: all 0.2s ease-in-out !important;
            color: #D1D5DB !important;
            font-weight: 500 !important;
            border-left: 3px solid transparent !important;
        }}

        [data-testid="stSidebarNav"] a:hover {{
            background-color: {acc_rgba} !important;
            color: #FFFFFF !important;
            transform: translateX(3px) !important;
            border-left: 3px solid {acc_light} !important;
        }}

        /* Item ativo / selecionado na Sidebar */
        [data-testid="stSidebarNav"] a[aria-current="page"],
        [data-testid="stSidebarNav"] li:has(a[aria-current="page"]) a {{
            background: linear-gradient(90deg, {acc_rgba} 0%, rgba(38, 39, 49, 0.4) 100%) !important;
            border-left: 3px solid {acc_hex} !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }}

        /* =========================================================
           3. BOTÕES
           ========================================================= */
        div.stButton > button,
        div[data-testid="stFormSubmitButton"] > button {{
            background-color: {acc_hex} !important;
            color: #FFFFFF !important;
            border: 1px solid {acc_hover} !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.25rem !important;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 2px 8px {acc_rgba} !important;
        }}

        div.stButton > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {{
            background-color: {acc_hover} !important;
            border-color: {acc_hover} !important;
            box-shadow: 0 4px 14px {acc_glow} !important;
            transform: translateY(-1px) !important;
        }}

        div.stButton > button:active,
        div[data-testid="stFormSubmitButton"] > button:active {{
            transform: translateY(0) !important;
        }}

        button[data-testid="baseButton-secondary"] {{
            background-color: #1F222E !important;
            border: 1px solid #373B4D !important;
            color: #D1D5DB !important;
            box-shadow: none !important;
        }}

        button[data-testid="baseButton-secondary"]:hover {{
            background-color: #282C3C !important;
            border-color: {acc_hex} !important;
            color: #FFFFFF !important;
        }}

        /* =========================================================
           4. CAMPOS DE FORMULÁRIO (INPUTS, SELECTS, TEXTAREAS)
           ========================================================= */
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
            background-color: {input_bg} !important;
            color: {text_title} !important;
            border: 1px solid {border_card} !important;
            border-radius: 8px !important;
            font-size: 0.95rem !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
        }}

        [data-testid="stTextInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus,
        [data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within > div {{
            border-color: {acc_hex} !important;
            box-shadow: 0 0 0 2px {acc_rgba} !important;
            outline: none !important;
        }}

        [data-testid="stTextInput"] input::placeholder,
        [data-testid="stTextArea"] textarea::placeholder {{
            color: {text_muted} !important;
        }}

        [data-testid="stWidgetLabel"] label,
        [data-testid="stWidgetLabel"] p {{
            color: {text_body} !important;
            font-weight: 500 !important;
            font-size: 0.88rem !important;
            margin-bottom: 0.25rem !important;
        }}

        /* =========================================================
           5. ABAS (TABS)
           ========================================================= */
        [data-testid="stTabs"] div[data-baseweb="tab-list"] {{
            border-bottom: 1px solid {border_subtle} !important;
            gap: 8px !important;
        }}

        [data-testid="stTabs"] button[data-baseweb="tab"] {{
            color: {text_muted} !important;
            font-weight: 500 !important;
            border-radius: 8px 8px 0 0 !important;
            padding: 10px 18px !important;
            background-color: transparent !important;
            border: none !important;
            transition: all 0.2s ease !important;
        }}

        [data-testid="stTabs"] button[data-baseweb="tab"]:hover {{
            color: {acc_light} !important;
            background-color: {acc_rgba} !important;
        }}

        [data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {{
            color: {text_title} !important;
            font-weight: 600 !important;
        }}

        [data-testid="stTabs"] div[data-baseweb="tab-highlight"] {{
            background-color: {acc_hex} !important;
            height: 3px !important;
            border-radius: 3px 3px 0 0 !important;
        }}

        /* =========================================================
           6. EXPANDERS E CONTAINERS
           ========================================================= */
        [data-testid="stExpander"] {{
            background-color: {bg_card} !important;
            border: 1px solid {border_card} !important;
            border-radius: 10px !important;
            margin-bottom: 12px !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25) !important;
            overflow: hidden !important;
        }}

        [data-testid="stExpander"] summary {{
            color: {text_title} !important;
            font-weight: 600 !important;
            padding: 12px 16px !important;
            transition: background-color 0.2s ease !important;
        }}

        [data-testid="stExpander"] summary:hover {{
            background-color: {acc_rgba} !important;
            color: {acc_light} !important;
        }}

        [data-testid="stExpander"] [data-testid="stExpanderDetails"] {{
            padding: 16px !important;
            border-top: 1px solid {border_subtle} !important;
            background-color: {bg_card} !important;
        }}

        /* =========================================================
           7. ALERTAS E MÉTRICAS
           ========================================================= */
        [data-testid="stAlert"] {{
            border-radius: 8px !important;
            background-color: {bg_card} !important;
            border-left-width: 4px !important;
        }}

        [data-testid="stMetric"] {{
            background-color: {bg_card} !important;
            border: 1px solid {border_card} !important;
            border-radius: 10px !important;
            padding: 1rem 1.25rem !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2) !important;
        }}

        [data-testid="stMetricLabel"] {{
            color: {text_muted} !important;
            font-weight: 500 !important;
            font-size: 0.85rem !important;
        }}

        [data-testid="stMetricValue"] {{
            color: {acc_light} !important;
            font-weight: 700 !important;
        }}

        /* =========================================================
           8. COMPONENTES EDUTrack AI (CABECALHO, CARDS, BADGES)
           ========================================================= */
        .edutrack-header-container {{
            margin-bottom: 1.75rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid {border_subtle};
        }}

        .edutrack-header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: {acc_rgba};
            color: {acc_light};
            border: 1px solid {acc_rgba};
            border-radius: 20px;
            padding: 4px 12px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            letter-spacing: 0.03em;
        }}

        .edutrack-header-title {{
            color: {text_title};
            font-size: 1.9rem;
            font-weight: 700;
            margin: 0.25rem 0 0.4rem 0;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .edutrack-header-subtitle {{
            color: {text_muted};
            font-size: 0.95rem;
            margin: 0;
            line-height: 1.4;
        }}

        .edutrack-card {{
            background-color: {bg_card};
            border: 1px solid {border_card};
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .edutrack-card:hover {{
            border-color: {acc_hex};
        }}

        .edutrack-badge {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.76rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }}

        .badge-purple {{
            background-color: {acc_rgba};
            color: {acc_light};
            border: 1px solid {acc_rgba};
        }}

        .badge-green {{
            background-color: rgba(16, 185, 129, 0.18);
            color: #34D399;
            border: 1px solid rgba(16, 185, 129, 0.35);
        }}

        .badge-amber {{
            background-color: rgba(245, 158, 11, 0.18);
            color: #FBBF24;
            border: 1px solid rgba(245, 158, 11, 0.35);
        }}

        .badge-red {{
            background-color: rgba(239, 68, 68, 0.18);
            color: #F87171;
            border: 1px solid rgba(239, 68, 68, 0.35);
        }}

        .badge-blue {{
            background-color: rgba(59, 130, 246, 0.18);
            color: #60A5FA;
            border: 1px solid rgba(59, 130, 246, 0.35);
        }}

        .badge-gray {{
            background-color: rgba(107, 114, 128, 0.2);
            color: #D1D5DB;
            border: 1px solid rgba(107, 114, 128, 0.35);
        }}

        .edutrack-meta-box {{
            background-color: {bg_card};
            border: 1px solid {border_card};
            border-radius: 8px;
            padding: 0.85rem 1rem;
            margin-bottom: 0.75rem;
        }}

        .edutrack-meta-label {{
            color: {text_muted};
            font-size: 0.8rem;
            font-weight: 500;
            margin-bottom: 2px;
        }}

        .edutrack-meta-value {{
            color: {text_title};
            font-size: 0.95rem;
            font-weight: 600;
        }}

        /* =========================================================
           9. COMPONENTES DO CALENDÁRIO
           ========================================================= */
        .calendar-grid {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 8px;
            margin-bottom: 1.5rem;
        }}

        .calendar-day-header {{
            text-align: center;
            font-weight: 700;
            font-size: 0.82rem;
            color: {acc_light};
            padding: 8px 0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .calendar-cell {{
            background-color: {bg_card};
            border: 1px solid {border_card};
            border-radius: 8px;
            padding: 8px;
            min-height: 72px;
            position: relative;
            transition: all 0.2s ease;
            cursor: pointer;
        }}

        .calendar-cell:hover {{
            border-color: {acc_hex};
            transform: translateY(-2px);
            box-shadow: 0 4px 12px {acc_rgba};
        }}

        .calendar-cell.is-today {{
            border: 2px solid {acc_hex};
            background: linear-gradient(135deg, {acc_rgba} 0%, {bg_card} 100%);
        }}

        .calendar-cell.is-selected {{
            border: 2px solid #38BDF8;
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
        }}

        .calendar-cell.is-empty {{
            background-color: transparent;
            border: 1px dashed {border_subtle};
            opacity: 0.3;
            cursor: default;
        }}

        .calendar-cell-number {{
            font-size: 0.9rem;
            font-weight: 700;
            color: {text_title};
            margin-bottom: 4px;
        }}

        .event-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 3px;
        }}

        .event-item-card {{
            background-color: {bg_card};
            border-left: 4px solid {acc_hex};
            border: 1px solid {border_card};
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 10px;
            transition: transform 0.2s ease;
        }}

        .event-item-card:hover {{
            transform: translateX(4px);
        }}

        /* =========================================================
           10. COMPONENTES DE CONQUISTAS E GAMIFICAÇÃO
           ========================================================= */
        .achievement-card {{
            background-color: {bg_card};
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            position: relative;
            overflow: hidden;
            border: 1px solid {border_card};
            transition: all 0.3s ease;
        }}

        .achievement-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        }}

        .rarity-comum {{
            border-left: 5px solid #9CA3AF !important;
        }}

        .rarity-rara {{
            border-left: 5px solid #3B82F6 !important;
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.15);
        }}

        .rarity-epica {{
            border-left: 5px solid #A855F7 !important;
            box-shadow: 0 0 18px rgba(168, 85, 247, 0.2);
        }}

        .rarity-lendaria {{
            border-left: 5px solid #F59E0B !important;
            box-shadow: 0 0 22px rgba(245, 158, 11, 0.25);
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.05) 0%, {bg_card} 100%);
        }}

        .achievement-locked {{
            opacity: 0.65;
            filter: grayscale(0.5);
        }}

        .progress-bar-container {{
            background-color: #232634;
            border-radius: 12px;
            height: 14px;
            width: 100%;
            overflow: hidden;
            margin: 8px 0;
            border: 1px solid #333748;
        }}

        .progress-bar-fill {{
            height: 100%;
            border-radius: 12px;
            background: linear-gradient(90deg, {acc_hex} 0%, #38BDF8 100%);
            transition: width 0.6s ease-in-out;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_page_header(title: str, subtitle: str, badge_text: str = "EduTrack AI", icon: str = ""):
    """Renderiza um cabeçalho de página moderno e padronizado."""
    accent = get_active_accent()
    icon_display = f"{icon} " if icon else ""
    st.markdown(
        f"""
        <div class="edutrack-header-container">
            <div class="edutrack-header-badge">✨ {badge_text}</div>
            <h1 class="edutrack-header-title">{icon_display}{title}</h1>
            <p class="edutrack-header-subtitle">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
