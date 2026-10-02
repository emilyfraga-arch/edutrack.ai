import os
import streamlit as st
from typing import List, Dict, Any, Optional

try:
    import requests
except ImportError:
    requests = None

# Configurações do Xano via variáveis de ambiente ou segredos do Streamlit
XANO_API_URL = os.getenv("XANO_API_URL", "")
XANO_AUTH_TOKEN = os.getenv("XANO_AUTH_TOKEN", "")

def _init_local_store():
    """Inicializa armazenamento local em sessão para modo de desenvolvimento ou fallback offline."""
    if "subjects_store" not in st.session_state:
        st.session_state.subjects_store = [
            {
                "id": 1,
                "name": "Cálculo I",
                "code": "MAT101",
                "professor": "Dr. Silva",
                "semester": "2026.1",
                "status": "active"
            },
            {
                "id": 2,
                "name": "Algoritmos e Estruturas de Dados",
                "code": "CC102",
                "professor": "Dra. Santos",
                "semester": "2026.1",
                "status": "active"
            }
        ]

def get_subjects(status: Optional[str] = "active") -> List[Dict[str, Any]]:
    """Obtém a lista de disciplinas (via Xano API ou fallback local)."""
    _init_local_store()

    if XANO_API_URL and requests is not None:
        try:
            headers = {"Authorization": f"Bearer {XANO_AUTH_TOKEN}"} if XANO_AUTH_TOKEN else {}
            params = {"status": status} if status else {}
            response = requests.get(f"{XANO_API_URL}/subjects", headers=headers, params=params, timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            st.sidebar.warning(f"⚠️ Modo offline ativo (Xano indisponível: {e})")

    # Fallback local
    items = st.session_state.subjects_store
    if status:
        return [item for item in items if item.get("status") == status]
    return list(items)

def create_subject(name: str, code: str = "", professor: str = "", semester: str = "") -> Optional[Dict[str, Any]]:
    """Cadastra uma nova disciplina (via Xano API ou fallback local)."""
    _init_local_store()

    payload = {
        "name": name.strip(),
        "code": code.strip(),
        "professor": professor.strip(),
        "semester": semester.strip()
    }

    if XANO_API_URL and requests is not None:
        try:
            headers = {"Authorization": f"Bearer {XANO_AUTH_TOKEN}"} if XANO_AUTH_TOKEN else {}
            response = requests.post(f"{XANO_API_URL}/subjects", json=payload, headers=headers, timeout=5)
            if response.status_code in [200, 201]:
                return response.json()
        except Exception as e:
            st.sidebar.warning(f"⚠️ Erro ao salvar no Xano ({e}), usando armazenamento local.")

    # Fallback local
    new_id = max([s["id"] for s in st.session_state.subjects_store], default=0) + 1
    new_subject = {
        "id": new_id,
        "name": payload["name"],
        "code": payload["code"],
        "professor": payload["professor"],
        "semester": payload["semester"],
        "status": "active"
    }
    st.session_state.subjects_store.append(new_subject)
    return new_subject

def delete_subject(subject_id: int) -> bool:
    """Remove ou arquiva uma disciplina por ID."""
    _init_local_store()

    if XANO_API_URL and requests is not None:
        try:
            headers = {"Authorization": f"Bearer {XANO_AUTH_TOKEN}"} if XANO_AUTH_TOKEN else {}
            response = requests.delete(f"{XANO_API_URL}/subjects/{subject_id}", headers=headers, timeout=5)
            if response.status_code in [200, 204]:
                return True
        except Exception:
            pass

    # Fallback local
    st.session_state.subjects_store = [
        s for s in st.session_state.subjects_store if s.get("id") != subject_id
    ]
    return True

