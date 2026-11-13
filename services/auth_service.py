import os
from typing import Tuple, Dict, Any, Optional
import requests

def get_base_url() -> str:
    """Carrega a URL base de autenticação do Xano a partir do arquivo .env ou variáveis de ambiente."""
    base_url = os.getenv("XANO_AUTH_BASE_URL")
    
    if not base_url:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(root_dir, ".env")
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() in ["XANO_AUTH_BASE_URL", "XANO_API_URL"]:
                            base_url = v.strip().strip('"').strip("'")
                            break
                    elif line.startswith("http"):
                        base_url = line.strip()
                        break
                        
    return (base_url or "").rstrip("/")

def get_api_url() -> str:
    """Carrega a URL base da API CRUD do Xano a partir do arquivo .env ou variáveis de ambiente."""
    api_url = os.getenv("XANO_API_URL")
    
    if not api_url:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_path = os.path.join(root_dir, ".env")
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() == "XANO_API_URL":
                            api_url = v.strip().strip('"').strip("'")
                            break
                            
    if not api_url:
        api_url = get_base_url()
        
    return (api_url or "").rstrip("/")

def signup(name: str, email: str, password: str) -> Tuple[bool, Dict[str, Any]]:
    """Cadastra um novo usuário no endpoint auth/signup do Xano."""
    base_url = get_base_url()
    if not base_url:
        return False, {"message": "URL base do Xano não configurada no arquivo .env."}
        
    url = f"{base_url}/auth/signup"
    payload = {
        "name": name.strip(),
        "email": email.strip().lower(),
        "password": password
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        data = response.json() if response.content else {}
        if response.status_code in [200, 201]:
            return True, data
        else:
            error_msg = data.get("message") or data.get("error") or f"Erro {response.status_code} ao cadastrar."
            return False, {"message": error_msg}
    except requests.exceptions.RequestException as e:
        return False, {"message": f"Erro de conexão com o servidor: {e}"}

def login(email: str, password: str) -> Tuple[bool, Dict[str, Any]]:
    """Realiza autenticação do usuário no endpoint auth/login do Xano."""
    base_url = get_base_url()
    if not base_url:
        return False, {"message": "URL base do Xano não configurada no arquivo .env."}
        
    url = f"{base_url}/auth/login"
    payload = {
        "email": email.strip().lower(),
        "password": password
    }
    
    try:
        print("URL de login:", url)  # Debugging line
        print(f"Attempting login with payload: {payload}")  # Debugging line

        response = requests.post(url, json=payload, timeout=10)
        data = response.json() if response.content else {}
        print(f"Login response: {data}")  # Debugging line
        if response.status_code == 200:
            return True, data
        else:
            error_msg = data.get("message") or data.get("error") or "Credenciais inválidas."
            return False, {"message": error_msg}
    except requests.exceptions.RequestException as e:
        return False, {"message": f"Erro de conexão com o servidor: {e}"}

def get_me(auth_token: str) -> Tuple[bool, Dict[str, Any]]:
    """Recupera os dados do usuário autenticado no endpoint auth/me do Xano."""
    base_url = get_base_url()
    if not base_url:
        return False, {"message": "URL base do Xano não configurada no arquivo .env."}
        
    url = f"{base_url}/auth/me"
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json() if response.content else {}
        if response.status_code == 200:
            return True, data
        else:
            error_msg = data.get("message") or data.get("error") or f"Erro {response.status_code} ao obter perfil."
            return False, {"message": error_msg}
    except requests.exceptions.RequestException as e:
        return False, {"message": f"Erro de conexão com o servidor: {e}"}

