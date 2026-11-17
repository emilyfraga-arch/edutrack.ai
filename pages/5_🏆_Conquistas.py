import streamlit as st
from styles.theme import apply_custom_theme, render_page_header, get_active_accent

# Configuração da Página
st.set_page_config(page_title="Conquistas - EduTrack AI", page_icon="🏆", layout="wide")

# Aplica Tema Visual Padronizado
apply_custom_theme()

active_accent = get_active_accent()

# Cabeçalho Padronizado
render_page_header(
    title="Conquistas & Medalhas",
    subtitle="Ganhe pontos de experiência (XP), suba de nível e colecione insígnias acadêmicas.",
    badge_text="Gamificação",
    icon="🏆"
)

# Níveis de Raridade e Estilos
RARITY_CONFIG = {
    "Comum": {
        "badge_class": "badge-gray",
        "border_color": "#9CA3AF",
        "glow": "rgba(156, 163, 175, 0.25)",
        "icon": "🥉",
        "card_class": "rarity-comum",
    },
    "Rara": {
        "badge_class": "badge-blue",
        "border_color": "#3B82F6",
        "glow": "rgba(59, 130, 246, 0.35)",
        "icon": "🥈",
        "card_class": "rarity-rara",
    },
    "Épica": {
        "badge_class": "badge-purple",
        "border_color": "#A855F7",
        "glow": "rgba(168, 85, 247, 0.4)",
        "icon": "🥇",
        "card_class": "rarity-epica",
    },
    "Lendária": {
        "badge_class": "badge-amber",
        "border_color": "#F59E0B",
        "glow": "rgba(245, 158, 11, 0.5)",
        "icon": "👑",
        "card_class": "rarity-lendaria",
    },
}

# Conquistas Demonstrativas Padrão
DEFAULT_ACHIEVEMENTS = [
    {
        "id": "first_step",
        "title": "Primeiro Passo",
        "rarity": "Comum",
        "description": "Conclua sua primeira tarefa acadêmica no sistema.",
        "xp": 50,
        "unlocked": True,
        "date_unlocked": "10/11/2026",
        "icon": "🚀",
    },
    {
        "id": "organized",
        "title": "Organizado",
        "rarity": "Comum",
        "description": "Cadastre pelo menos 3 disciplinas ativas no semestre letivo.",
        "xp": 75,
        "unlocked": True,
        "date_unlocked": "12/11/2026",
        "icon": "📚",
    },
    {
        "id": "full_focus",
        "title": "Foco Total",
        "rarity": "Rara",
        "description": "Mantenha uma sequência de 5 dias seguidos com tarefas e estudos.",
        "xp": 150,
        "unlocked": True,
        "date_unlocked": "15/11/2026",
        "icon": "🔥",
    },
    {
        "id": "subject_master",
        "title": "Mestre das Disciplinas",
        "rarity": "Épica",
        "description": "Conclua 100% de todas as atividades e trabalhos de uma disciplina.",
        "xp": 250,
        "unlocked": True,
        "date_unlocked": "16/11/2026",
        "icon": "🎓",
    },
    {
        "id": "punctuality",
        "title": "Pontualidade Britânica",
        "rarity": "Rara",
        "description": "Entregue 3 tarefas com antecedência mínima de 24 horas do prazo.",
        "xp": 150,
        "unlocked": False,
        "progress": "2 / 3 entregas",
        "icon": "⏱️",
    },
    {
        "id": "early_bird",
        "title": "Madrugador Acadêmico",
        "rarity": "Rara",
        "description": "Revise resumos ou conclua pendências acadêmicas antes das 8h da manhã.",
        "xp": 120,
        "unlocked": False,
        "progress": "0 / 1 dia",
        "icon": "🌅",
    },
    {
        "id": "marathon",
        "title": "Maratona do Conhecimento",
        "rarity": "Épica",
        "description": "Acumule mais de 20 horas de estudos registrados e focados.",
        "xp": 300,
        "unlocked": False,
        "progress": "14 / 20 horas",
        "icon": "🧠",
    },
    {
        "id": "golden_student",
        "title": "Estudante de Ouro",
        "rarity": "Lendária",
        "description": "Desbloqueie todas as medalhas e atinja o patamar de excelência acadêmica.",
        "xp": 500,
        "unlocked": False,
        "progress": "4 / 8 medalhas",
        "icon": "👑",
    },
]

# Inicializa Estado Local das Conquistas
if "user_achievements" not in st.session_state:
    st.session_state["user_achievements"] = [dict(a) for a in DEFAULT_ACHIEVEMENTS]

# Mensagem Comemorativa Temporária
if "celebration_msg" not in st.session_state:
    st.session_state["celebration_msg"] = None

# Calcula Estatísticas Atuais
achievements = st.session_state["user_achievements"]
unlocked_count = sum(1 for a in achievements if a.get("unlocked"))
total_count = len(achievements)
total_xp = sum(a.get("xp", 0) for a in achievements if a.get("unlocked"))

# Nível com base no XP (cada 200 XP = 1 nível)
level = max(1, (total_xp // 200) + 1)
level_titles = [
    "Iniciante Dedicado",
    "Estudante Focado",
    "Estrategista Acadêmico",
    "Pesquisador Notável",
    "Grão-Mestre do Conhecimento",
]
level_title = level_titles[min(level - 1, len(level_titles) - 1)]

xp_current_bracket = total_xp % 200
xp_next_level = 200
progress_pct = int((xp_current_bracket / xp_next_level) * 100)

# Exibe Mensagem Comemorativa e Animação se Ativa
if st.session_state["celebration_msg"]:
    st.balloons()
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.25) 0%, rgba(139, 92, 246, 0.25) 100%); border: 2px solid #F59E0B; border-radius: 12px; padding: 18px 24px; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(245, 158, 11, 0.35); text-align: center;">
            <div style="font-size: 1.6rem; font-weight: 800; color: #FBBF24; margin-bottom: 4px;">🎉 CONQUISTA DESBLOQUEADA! 🎉</div>
            <div style="font-size: 1.15rem; font-weight: 600; color: #FFFFFF;">{st.session_state['celebration_msg']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Limpa para a próxima interação
    st.session_state["celebration_msg"] = None

# Painel de Nível e Progresso
st.markdown(
    f"""
    <div class="edutrack-card" style="margin-bottom: 1.5rem; background: linear-gradient(135deg, #161922 0%, #1A1D29 100%);">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 12px;">
            <div>
                <div style="font-size: 0.85rem; color: #9CA3AF; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700;">Progresso Geral do Estudante</div>
                <div style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; display: flex; align-items: center; gap: 10px;">
                    ⭐ Nível {level} • <span style="color: {active_accent['light']}; font-weight: 600;">{level_title}</span>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.35rem; font-weight: 800; color: #38BDF8;">{total_xp} XP</div>
                <div style="font-size: 0.8rem; color: #9CA3AF;">Próximo nível em {xp_next_level - xp_current_bracket} XP</div>
            </div>
        </div>
        <div class="progress-bar-container">
            <div class="progress-bar-fill" style="width: {progress_pct}%;"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #9CA3AF; margin-top: 4px;">
            <span>{xp_current_bracket} XP</span>
            <span>{progress_pct}% concluído</span>
            <span>{xp_next_level} XP</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Métricas Visuais
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric("Medalhas Conquistadas", f"{unlocked_count} / {total_count}")
with col_m2:
    st.metric("Total de XP", f"{total_xp} XP")
with col_m3:
    st.metric("Sequência de Estudos", "🔥 5 Dias")
with col_m4:
    st.metric("Raridade Mais Alta", "🥇 Épica")

st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

# Abas de Filtro das Conquistas
tab_all, tab_unlocked, tab_locked, tab_actions = st.tabs([
    f"🏆 Todas as Medalhas ({total_count})",
    f"✅ Desbloqueadas ({unlocked_count})",
    f"🔒 A Conquistar ({total_count - unlocked_count})",
    "🎯 Interação & Testes"
])

def render_achievement_card(ach: dict):
    """Renderiza o card de uma conquista com suporte a raridade e status."""
    is_unlocked = ach.get("unlocked", False)
    rarity = ach.get("rarity", "Comum")
    r_cfg = RARITY_CONFIG.get(rarity, RARITY_CONFIG["Comum"])

    card_class = f"achievement-card {r_cfg['card_class']}"
    if not is_unlocked:
        card_class += " achievement-locked"

    status_badge = (
        f"<span class='edutrack-badge badge-green'>✓ Conquistada • {ach.get('date_unlocked', 'Recente')}</span>"
        if is_unlocked
        else f"<span class='edutrack-badge badge-gray'>🔒 Bloqueada ({ach.get('progress', 'Pendente')})</span>"
    )

    st.markdown(
        f"""
        <div class="{card_class}">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px;">
                <div style="display: flex; gap: 16px; align-items: center;">
                    <div style="font-size: 2.2rem; width: 54px; height: 54px; border-radius: 12px; background: rgba(255, 255, 255, 0.05); display: flex; align-items: center; justify-content: center; border: 1px solid {r_cfg['border_color']}; box-shadow: 0 0 12px {r_cfg['glow']};">
                        {ach.get('icon', '🎖️')}
                    </div>
                    <div>
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 2px;">
                            <span style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF;">{ach.get('title')}</span>
                            <span class="edutrack-badge {r_cfg['badge_class']}">{r_cfg['icon']} {rarity}</span>
                        </div>
                        <div style="font-size: 0.88rem; color: #D1D5DB; margin-bottom: 6px;">
                            {ach.get('description')}
                        </div>
                        <div>
                            {status_badge}
                        </div>
                    </div>
                </div>
                <div style="text-align: right; min-width: 90px;">
                    <div style="font-size: 1.1rem; font-weight: 800; color: #FCD34D;">+{ach.get('xp')} XP</div>
                    <div style="font-size: 0.75rem; color: #9CA3AF;">Recompensa</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab_all:
    for a in achievements:
        render_achievement_card(a)

with tab_unlocked:
    unlocked_list = [a for a in achievements if a.get("unlocked")]
    if not unlocked_list:
        st.info("Nenhuma conquista desbloqueada ainda. Complete desafios para conquistar suas medalhas!")
    else:
        for a in unlocked_list:
            render_achievement_card(a)

with tab_locked:
    locked_list = [a for a in achievements if not a.get("unlocked")]
    if not locked_list:
        st.success("🎉 Incrível! Você conquistou todas as medalhas disponíveis no EduTrack AI!")
    else:
        for a in locked_list:
            render_achievement_card(a)

with tab_actions:
    st.markdown("### 🎯 Demonstração Interativa de Desbloqueio")
    st.caption("Teste em tempo real como o sistema reage ao conquistar uma nova medalha acadêmica, com animações e mensagens comemorativas.")

    locked_options = [a for a in st.session_state["user_achievements"] if not a.get("unlocked")]

    if locked_options:
        col_act1, col_act2 = st.columns([2, 1])
        with col_act1:
            chosen_to_unlock = st.selectbox(
                "Escolha uma conquista para desbloquear:",
                [a["title"] for a in locked_options],
                key="select_ach_to_unlock"
            )
        with col_act2:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            if st.button("✨ Desbloquear Conquista Agora!", key="btn_unlock_achievement"):
                for a in st.session_state["user_achievements"]:
                    if a["title"] == chosen_to_unlock:
                        a["unlocked"] = True
                        a["date_unlocked"] = "Hoje"
                        st.session_state["celebration_msg"] = f"Você conquistou a medalha '{a['title']}' e recebeu +{a['xp']} XP!"
                        st.rerun()
    else:
        st.success("Todas as medalhas já foram desbloqueadas na demonstração!")

    st.markdown("---")
    st.markdown("#### Reiniciar Demonstração")
    st.caption("Restaure as medalhas e pontuações para o estado inicial demonstrativo.")
    if st.button("🔄 Redefinir Conquistas para o Padrão", key="btn_reset_achievements"):
        st.session_state["user_achievements"] = [dict(a) for a in DEFAULT_ACHIEVEMENTS]
        st.session_state["celebration_msg"] = None
        st.success("Conquistas redefinidas para o estado demonstrativo inicial.")
        st.rerun()
