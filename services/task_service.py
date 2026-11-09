import os
from typing import Tuple, List, Dict, Any, Optional
import requests
from services.auth_service import get_api_url

def get_academic_tasks(token: Optional[str] = None, subject_id: Optional[int] = None, status: Optional[str] = None) -> Tuple[bool, Any]:
    """Obtém a lista de tarefas acadêmicas da tabela academic_tasks do Xano para o usuário autenticado."""
    if not token:
        return False, "Usuário não autenticado. Faça login para visualizar suas tarefas."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/academic_tasks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {}
    if subject_id:
        params["subject_id"] = subject_id
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
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao buscar tarefas."
            except Exception:
                msg = f"Erro {response.status_code} ao buscar tarefas."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao buscar tarefas no servidor Xano."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def get_academic_task_by_id(task_id: int, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Recupera os detalhes de uma tarefa acadêmica específica da tabela academic_tasks do Xano."""
    if not token:
        return False, "Usuário não autenticado. Faça login para consultar a tarefa."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/academic_tasks/{task_id}"
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
            return False, "Tarefa acadêmica não encontrada ou não pertence ao usuário."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao buscar detalhes da tarefa."
            except Exception:
                msg = f"Erro {response.status_code} ao buscar detalhes da tarefa."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao contatar o servidor Xano."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def create_academic_task(title: str, description: str = "", due_date: str = "", status: str = "Pendente", subject_id: Optional[int] = None, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Cadastra uma nova tarefa acadêmica na tabela academic_tasks do Xano para o usuário autenticado."""
    if not token:
        return False, "Usuário não autenticado. Faça login para cadastrar tarefas."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/academic_tasks"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "status": status.strip()
    }
    if subject_id is not None:
        payload["subject_id"] = subject_id

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
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao criar tarefa."
            except Exception:
                msg = f"Erro {response.status_code} ao criar tarefa."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao cadastrar tarefa."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def update_academic_task(task_id: int, data: Dict[str, Any], token: Optional[str] = None) -> Tuple[bool, Any]:
    """Atualiza dados de uma tarefa acadêmica na tabela academic_tasks do Xano."""
    if not token:
        return False, "Usuário não autenticado."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/academic_tasks/{task_id}"
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
            return False, "Tarefa não encontrada ou não pertence ao usuário."
        else:
            try:
                err_data = response.json()
                msg = err_data.get("message") or err_data.get("error") or f"Erro {response.status_code} ao atualizar tarefa."
            except Exception:
                msg = f"Erro {response.status_code} ao atualizar tarefa."
            return False, msg
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao atualizar tarefa."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"

def update_task_status(task_id: int, status: str, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Atualiza o status de uma tarefa acadêmica na tabela academic_tasks do Xano."""
    return update_academic_task(task_id=task_id, data={"status": status.strip()}, token=token)

def delete_academic_task(task_id: int, token: Optional[str] = None) -> Tuple[bool, Any]:
    """Remove uma tarefa acadêmica na tabela academic_tasks do Xano."""
    if not token:
        return False, "Usuário não autenticado."

    api_url = get_api_url()
    if not api_url:
        return False, "URL base da API não configurada no arquivo .env."

    url = f"{api_url}/academic_tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.delete(url, headers=headers, timeout=10)
        if response.status_code in [200, 204]:
            return True, "Tarefa removida com sucesso."
        elif response.status_code == 401:
            return False, "Sessão expirada ou não autorizada. Faça login novamente."
        elif response.status_code == 404:
            return False, "Tarefa não encontrada ou não pertence ao usuário."
        else:
            return False, f"Erro {response.status_code} ao remover tarefa."
    except requests.exceptions.Timeout:
        return False, "Tempo limite de conexão esgotado ao remover tarefa."
    except requests.exceptions.RequestException as e:
        return False, f"Falha de conexão com o servidor Xano: {e}"
