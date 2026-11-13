import os
import sys
import json
import argparse
from typing import Dict, Any, Optional, Tuple

import requests

# Adiciona o diretório raiz ao sys.path para importar services
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from services.auth_service import get_api_url, get_base_url


def calculate_subject_progress(
    subject_id: int,
    token: Optional[str] = None,
    base_url: Optional[str] = None
) -> Dict[str, Any]:
    """
    Calcula a porcentagem de progresso (concluídas / total) de uma disciplina
    baseando-se em suas tarefas acadêmicas consultadas via endpoints CRUD do Xano.
    Retorna um dicionário estruturado pronto para serialização em JSON.
    """
    if not token:
        token = os.getenv("AUTH_TOKEN")

    if not token:
        return {
            "subject_id": subject_id,
            "error": "Token de autenticação não fornecido. Use --token ou defina AUTH_TOKEN."
        }

    api_base = base_url or get_api_url() or get_base_url()
    if not api_base:
        return {
            "subject_id": subject_id,
            "error": "URL base da API não configurada no arquivo .env."
        }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        # 1. Consulta detalhes da disciplina
        subject_url = f"{api_base}/subjects/{subject_id}"
        subj_response = requests.get(subject_url, headers=headers, timeout=10)

        if subj_response.status_code == 401:
            return {
                "subject_id": subject_id,
                "error": "Sessão expirada ou não autorizada. Faça login novamente."
            }
        elif subj_response.status_code == 404:
            return {
                "subject_id": subject_id,
                "error": f"Disciplina com ID {subject_id} não encontrada ou não pertence ao usuário."
            }
        elif subj_response.status_code != 200:
            return {
                "subject_id": subject_id,
                "error": f"Erro {subj_response.status_code} ao buscar dados da disciplina."
            }

        subject_data = subj_response.json() if subj_response.content else {}
        subject_name = subject_data.get("name") or f"Disciplina {subject_id}"

        # 2. Consulta as tarefas acadêmicas associadas
        tasks_url = f"{api_base}/academic_tasks"
        tasks_response = requests.get(tasks_url, headers=headers, params={"subject_id": subject_id}, timeout=10)

        if tasks_response.status_code != 200:
            return {
                "subject_id": subject_id,
                "subject_name": subject_name,
                "error": f"Erro {tasks_response.status_code} ao consultar tarefas da disciplina."
            }

        raw_tasks = tasks_response.json() if tasks_response.content else []
        if isinstance(raw_tasks, dict):
            raw_tasks = [raw_tasks]

        # Filtra tarefas vinculadas à disciplina informada
        subject_tasks = [
            t for t in raw_tasks
            if t.get("subject_id") == subject_id
        ] if raw_tasks else []

        # 3. Cálculo de métricas e porcentagem de progresso
        total_tasks = len(subject_tasks)
        completed_tasks = sum(
            1 for t in subject_tasks
            if str(t.get("status", "")).strip().lower() in ["concluída", "concluida", "completed", "done"]
        )
        pending_tasks = total_tasks - completed_tasks

        progress_percentage = round((completed_tasks / total_tasks * 100), 2) if total_tasks > 0 else 0.0

        return {
            "subject_id": subject_id,
            "subject_name": subject_name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "progress_percentage": progress_percentage
        }

    except requests.exceptions.Timeout:
        return {
            "subject_id": subject_id,
            "error": "Tempo limite de conexão esgotado ao contatar o servidor Xano."
        }
    except requests.exceptions.RequestException as e:
        return {
            "subject_id": subject_id,
            "error": f"Falha de conexão com o servidor Xano: {e}"
        }


def calculate_sample_progress(subject_id: int = 1) -> Dict[str, Any]:
    """Retorna cálculo de progresso com dados de exemplo para testes offline."""
    return {
        "subject_id": subject_id,
        "subject_name": "Banco de Dados Relacional",
        "total_tasks": 4,
        "completed_tasks": 3,
        "pending_tasks": 1,
        "progress_percentage": 75.0
    }


def get_progress_json(
    subject_id: int,
    token: Optional[str] = None,
    base_url: Optional[str] = None,
    sample: bool = False,
    indent: int = 2
) -> str:
    """Executa o cálculo de progresso e retorna a string formatada em JSON."""
    if sample:
        result = calculate_sample_progress(subject_id)
    else:
        result = calculate_subject_progress(subject_id=subject_id, token=token, base_url=base_url)

    return json.dumps(result, ensure_ascii=False, indent=indent)


def main():
    parser = argparse.ArgumentParser(
        description="Calcula a porcentagem de progresso de uma disciplina baseada em suas tarefas (EduTrack AI)."
    )
    parser.add_argument(
        "--subject-id", "-s",
        type=int,
        default=None,
        help="ID da disciplina a ter o progresso calculado"
    )
    parser.add_argument(
        "--token", "-t",
        default=None,
        help="Token de autenticação JWT do usuário"
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="URL base personalizada dos endpoints do Xano"
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Executa o cálculo com dados de exemplo offline"
    )

    args = parser.parse_args()

    if not args.sample and args.subject_id is None:
        parser.error("O argumento --subject-id é obrigatório (a menos que utilize --sample).")

    subject_id = args.subject_id or 1
    json_output = get_progress_json(
        subject_id=subject_id,
        token=args.token,
        base_url=args.base_url,
        sample=args.sample
    )

    print(json_output)


if __name__ == "__main__":
    main()
