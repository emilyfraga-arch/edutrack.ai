import os
from typing import Tuple, List, Dict, Any, Optional
import requests
from services.auth_service import get_api_url

def get_subjects(token: Optional[str] = None, status: Optional[str] = None) -> Tuple[bool, Any]:
    """Obtém a lista de disciplinas da tabela subjects do Xano para o usuário autenticado."""
    if not token:
        return False, "Usuário não autenticado. Faça login para visualizar suas disciplinas."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/subjects"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {}
    if status:
        params["status"] = status

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json() if response.content else []
            if isinstance(data, list):
                return True, data
            return True, [data]
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao buscar disciplinas."
            except Exception:
                msg = f"Erro {response.status_code} ao buscar disciplinas."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao contatar o servidor Xano."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def get_subject_by_id(subject_id: int, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Recupera os detalhes de uma disciplina específica da tabela subjects do Xano."""
    if not token:
        return False, "Usuário não autenticado. Faça login para consultar a disciplina."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/subjects/{subject_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json() if response.content else {}
            return True, data
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        elif response.status_code == 404:
            return False, "Disciplina não encontrada ou não pertence ao usuário."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao buscar detalhes da disciplina."
            except Exception:
                msg = f"Erro {response.status_code} ao buscar detalhes da disciplina."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao contatar o servidor Xano."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def create_subject(name: str, code: str = "", professor: str = "", semester: str = "", token: Optional[str] = None) -> Tuple[bool, Any]:
    """Cadastra uma nova disciplina na tabela subjects do Xano para o usuário autenticado."""
    if not token:
        return False, "Usuário não autenticado. Faça login para cadastrar disciplinas."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/subjects"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "name": name.strip(),
        "code": code.strip(),
        "professor": professor.strip(),
        "semester": semester.strip()
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code in [200, 201]:
            data = response.json() if response.content else {}
            return True, data
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao cadastrar disciplina."
            except Exception:
                msg = f"Erro {response.status_code} ao cadastrar disciplina."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao cadastrar disciplina."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def update_subject(subject_id: int, data: Dict[str, Any], token: Optional[str] = None) -> Tuple[bool, Any]:
    """Atualiza dados de uma disciplina existente na tabela subjects do Xano."""
    if not token:
        return False, "Usuário não autenticado. Faça login para atualizar disciplinas."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/subjects/{subject_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.patch(url, json=data, headers=headers, timeout=10)
        if response.status_code in [200, 204]:
            res_data = response.json() if response.content else {"success": True}
            return True, res_data
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        elif response.status_code == 404:
            return False, "Disciplina não encontrada ou não pertence ao usuário."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao atualizar disciplina."
            except Exception:
                msg = f"Erro {response.status_code} ao atualizar disciplina."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao atualizar disciplina."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def delete_subject(subject_id: int, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Remove uma disciplina na tabela subjects do Xano."""
    if not token:
        return False, "Usuário não autenticado."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/subjects/{subject_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.delete(url, headers=headers, timeout=10)
        if response.status_code in [200, 204]:
            return True, "Disciplina removida com sucesso."
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        elif response.status_code == 404:
            return False, "Disciplina não encontrada ou não pertence ao usuário."
        else:
            return False, f"Erro {response.status_code} ao remover disciplina."
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao excluir disciplina."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"
