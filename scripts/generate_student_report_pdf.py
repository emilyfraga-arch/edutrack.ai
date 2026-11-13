import os
import sys
import io
import json
import argparse
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

import requests

# Adiciona o diretório raiz ao sys.path para importar services
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from services.auth_service import get_api_url, get_base_url


class PDFCanvas:
    """Gerador vetorial de PDF minimalista em Python puro sem dependências externas."""
    def __init__(self, width: float = 595.28, height: float = 841.89):
        self.width = width
        self.height = height
        self.pages: List[bytes] = []
        self._current_page: List[bytes] = []
        self._font_names = {
            "F1": "Helvetica",
            "F2": "Helvetica-Bold",
            "F3": "Helvetica-Oblique"
        }

    def new_page(self):
        if self._current_page:
            self.pages.append(b"\n".join(self._current_page))
            self._current_page = []

    def set_fill_color(self, r: float, g: float, b: float):
        self._current_page.append(f"{r:.3f} {g:.3f} {b:.3f} rg".encode("latin-1"))

    def set_stroke_color(self, r: float, g: float, b: float):
        self._current_page.append(f"{r:.3f} {g:.3f} {b:.3f} RG".encode("latin-1"))

    def set_line_width(self, width: float):
        self._current_page.append(f"{width:.2f} w".encode("latin-1"))

    def rect(self, x: float, y: float, w: float, h: float, fill: bool = True, stroke: bool = False):
        op = "B" if fill and stroke else ("f" if fill else "S")
        self._current_page.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}".encode("latin-1"))

    def line(self, x1: float, y1: float, x2: float, y2: float):
        self._current_page.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S".encode("latin-1"))

    def draw_text(self, x: float, y: float, text: str, font: str = "F1", size: float = 12):
        clean_text = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        clean_text = clean_text.encode("latin-1", "replace").decode("latin-1")
        cmd = f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({clean_text}) Tj ET"
        self._current_page.append(cmd.encode("latin-1"))

    def output(self) -> bytes:
        if self._current_page:
            self.pages.append(b"\n".join(self._current_page))
            self._current_page = []
        if not self.pages:
            self.pages.append(b"")

        out = io.BytesIO()
        out.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = {}

        # 1: Catalog
        offsets[1] = out.tell()
        out.write(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")

        # 2: Pages
        page_count = len(self.pages)
        kids = " ".join(f"{4 + i * 2} 0 R" for i in range(page_count))
        offsets[2] = out.tell()
        out.write(f"2 0 obj\n<< /Type /Pages /Kids [{kids}] /Count {page_count} >>\nendobj\n".encode("latin-1"))

        font_objs = {}
        curr_obj_id = 4 + page_count * 2
        for fid, fname in self._font_names.items():
            font_objs[fid] = curr_obj_id
            curr_obj_id += 1

        for i, page_stream in enumerate(self.pages):
            page_obj = 4 + i * 2
            content_obj = page_obj + 1

            font_res = " ".join(f"/{fid} {oid} 0 R" for fid, oid in font_objs.items())
            offsets[page_obj] = out.tell()
            out.write(
                f"{page_obj} 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.width:.2f} {self.height:.2f}] "
                f"/Contents {content_obj} 0 R /Resources << /Font << {font_res} >> >> >>\nendobj\n".encode("latin-1")
            )

            offsets[content_obj] = out.tell()
            out.write(f"{content_obj} 0 obj\n<< /Length {len(page_stream)} >>\nstream\n".encode("latin-1"))
            out.write(page_stream)
            out.write(b"\nendstream\nendobj\n")

        for fid, fname in self._font_names.items():
            oid = font_objs[fid]
            offsets[oid] = out.tell()
            out.write(
                f"{oid} 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /{fname} /Encoding /WinAnsiEncoding >>\nendobj\n".encode(
                    "latin-1"
                )
            )

        total_objects = curr_obj_id
        startxref = out.tell()
        out.write(f"xref\n0 {total_objects}\n0000000000 65535 f \n".encode("latin-1"))
        for oid in range(1, total_objects):
            offset = offsets.get(oid, 0)
            out.write(f"{offset:010d} 00000 n \n".encode("latin-1"))

        out.write(f"trailer\n<< /Size {total_objects} /Root 1 0 R >>\nstartxref\n{startxref}\n%%EOF\n".encode("latin-1"))
        return out.getvalue()


def fetch_report_data(token: Optional[str] = None, base_url: Optional[str] = None) -> Tuple[bool, Dict[str, Any]]:
    """Busca os dados de desempenho acadêmico através dos endpoints do Xano."""
    if not token:
        token = os.getenv("AUTH_TOKEN")

    if not token:
        return False, {"error": "Token de autenticação não fornecido. Use --token ou defina AUTH_TOKEN."}

    api_base = base_url or get_api_url() or get_base_url()
    if not api_base:
        return False, {"error": "URL base do Xano não configurada no arquivo .env."}

    headers = {"Authorization": f"Bearer {token}"}

    # 1. Tenta consumir o endpoint dedicado de relatório de desempenho
    report_endpoint = f"{api_base}/reports/student_performance_pdf"
    try:
        res = requests.get(report_endpoint, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, dict) and "student" in data:
                return True, data
    except requests.exceptions.RequestException:
        pass

    # 2. Fallback resiliente: agrega através dos endpoints CRUD existentes
    try:
        # Perfil do aluno
        me_res = requests.get(f"{api_base}/auth/me", headers=headers, timeout=10)
        student_data = me_res.json() if me_res.status_code == 200 else {"name": "Aluno", "email": "aluno@edutrack.ai"}

        # Disciplinas
        subj_res = requests.get(f"{api_base}/subjects", headers=headers, timeout=10)
        subjects = subj_res.json() if subj_res.status_code == 200 and isinstance(subj_res.json(), list) else []

        # Tarefas acadêmicas
        task_res = requests.get(f"{api_base}/academic_tasks", headers=headers, timeout=10)
        tasks = task_res.json() if task_res.status_code == 200 and isinstance(task_res.json(), list) else []

        return True, {
            "student": student_data,
            "subjects": subjects,
            "academic_tasks": tasks,
            "report_title": "EduTrack AI - Relatório de Desempenho Acadêmico"
        }
    except requests.exceptions.RequestException as e:
        return False, {"error": f"Falha de conexão com o servidor Xano: {e}"}


def get_sample_report_data() -> Dict[str, Any]:
    """Retorna dados de exemplo para geração offline do relatório."""
    return {
        "student": {
            "id": 1,
            "name": "Maria Silva",
            "email": "maria.silva@aluno.impacta.edu.br"
        },
        "subjects": [
            {
                "id": 101,
                "name": "Banco de Dados Relacional",
                "code": "BDR-201",
                "professor": "Prof. Carlos Eduardo",
                "semester": "2026/2"
            },
            {
                "id": 102,
                "name": "Inteligência Artificial Aplicada",
                "code": "IAA-301",
                "professor": "Profa. Fernanda Lima",
                "semester": "2026/2"
            },
            {
                "id": 103,
                "name": "Engenharia de Software",
                "code": "ESW-104",
                "professor": "Prof. Roberto Santos",
                "semester": "2026/2"
            }
        ],
        "academic_tasks": [
            {
                "id": 1,
                "subject_id": 101,
                "title": "Modelagem de Entidade-Relacionamento",
                "due_date": "2026-11-20",
                "status": "Concluída"
            },
            {
                "id": 2,
                "subject_id": 101,
                "title": "Normalização e Scripts DDL",
                "due_date": "2026-11-28",
                "status": "Pendente"
            },
            {
                "id": 3,
                "subject_id": 102,
                "title": "Implementação de Regressão Linear em Python",
                "due_date": "2026-11-15",
                "status": "Concluída"
            },
            {
                "id": 4,
                "subject_id": 102,
                "title": "Artigo sobre Redes Neurais Convolucionais",
                "due_date": "2026-12-05",
                "status": "Concluída"
            },
            {
                "id": 5,
                "subject_id": 103,
                "title": "Documento de Especificação de Requisitos",
                "due_date": "2026-11-25",
                "status": "Pendente"
            }
        ],
        "report_title": "EduTrack AI - Relatório de Desempenho Acadêmico"
    }


def render_student_report_pdf(report_data: Dict[str, Any]) -> bytes:
    """Renderiza os dados do relatório em formato PDF vetorial estilizado."""
    canvas = PDFCanvas(width=595.28, height=841.89)  # A4

    student = report_data.get("student") or {}
    subjects = report_data.get("subjects") or []
    tasks = report_data.get("academic_tasks") or []

    student_name = student.get("name") or "Estudante"
    student_email = student.get("email") or "Não informado"
    emission_date = datetime.now().strftime("%d/%m/%Y às %H:%M")

    # Cálculos quantitativos de progresso
    total_subjects = len(subjects)
    total_tasks = len(tasks)
    completed_tasks = sum(
        1 for t in tasks if str(t.get("status", "")).strip().lower() in ["concluída", "concluida", "completed", "done"]
    )
    pending_tasks = total_tasks - completed_tasks
    overall_progress = round((completed_tasks / total_tasks * 100), 1) if total_tasks > 0 else 0.0

    current_page = 1

    def draw_header_footer(page_num: int):
        # Banner de cabeçalho superior (Azul EduTrack #1E3A8A)
        canvas.set_fill_color(0.12, 0.23, 0.54)
        canvas.rect(40, 770, 515, 45, fill=True, stroke=False)

        canvas.set_fill_color(1.0, 1.0, 1.0)
        canvas.draw_text(55, 795, "EduTrack AI", font="F2", size=18)
        canvas.draw_text(55, 780, "Relatório Consolidado de Desempenho Acadêmico", font="F1", size=10)

        # Rodapé
        canvas.set_stroke_color(0.85, 0.85, 0.85)
        canvas.set_line_width(0.8)
        canvas.line(40, 45, 555, 45)

        canvas.set_fill_color(0.5, 0.5, 0.5)
        canvas.draw_text(40, 32, f"Emitido em: {emission_date}", font="F1", size=8)
        canvas.draw_text(495, 32, f"Página {page_num}", font="F1", size=8)

    draw_header_footer(current_page)

    y = 745

    # 1. Informações do Estudante
    canvas.set_fill_color(0.96, 0.97, 0.99)
    canvas.set_stroke_color(0.80, 0.85, 0.95)
    canvas.set_line_width(1)
    canvas.rect(40, y - 55, 515, 55, fill=True, stroke=True)

    canvas.set_fill_color(0.12, 0.23, 0.54)
    canvas.draw_text(55, y - 18, "DADOS DO ESTUDANTE", font="F2", size=10)

    canvas.set_fill_color(0.2, 0.2, 0.2)
    canvas.draw_text(55, y - 35, f"Nome: {student_name}", font="F1", size=10)
    canvas.draw_text(55, y - 48, f"E-mail: {student_email}", font="F1", size=10)

    y -= 75

    # 2. Resumo de Progresso e Métricas
    canvas.set_fill_color(0.12, 0.23, 0.54)
    canvas.draw_text(40, y, "RESUMO GERAL DE DESEMPENHO", font="F2", size=12)
    y -= 15

    # Cards de métricas
    card_width = 120
    card_height = 42
    cards = [
        ("Disciplinas", str(total_subjects), (0.93, 0.95, 0.98)),
        ("Total Tarefas", str(total_tasks), (0.93, 0.95, 0.98)),
        ("Concluídas", str(completed_tasks), (0.88, 0.96, 0.89)),
        ("Pendentes", str(pending_tasks), (0.99, 0.94, 0.90)),
    ]

    for idx, (label, val, bg_color) in enumerate(cards):
        cx = 40 + idx * (card_width + 11.5)
        canvas.set_fill_color(*bg_color)
        canvas.rect(cx, y - card_height, card_width, card_height, fill=True, stroke=False)

        canvas.set_fill_color(0.4, 0.4, 0.4)
        canvas.draw_text(cx + 10, y - 15, label, font="F1", size=8)

        canvas.set_fill_color(0.12, 0.23, 0.54)
        canvas.draw_text(cx + 10, y - 35, val, font="F2", size=16)

    y -= (card_height + 20)

    # Barra de Progresso Geral
    canvas.set_fill_color(0.2, 0.2, 0.2)
    canvas.draw_text(40, y, f"Aproveitamento Geral: {overall_progress}%", font="F2", size=10)
    y -= 12

    # Fundo da barra
    bar_width = 515
    bar_height = 10
    canvas.set_fill_color(0.90, 0.90, 0.90)
    canvas.rect(40, y - bar_height, bar_width, bar_height, fill=True, stroke=False)

    # Preenchimento proporcional da barra
    if overall_progress > 0:
        fill_w = (overall_progress / 100.0) * bar_width
        canvas.set_fill_color(0.10, 0.65, 0.35)  # Verde esmeralda
        canvas.rect(40, y - bar_height, fill_w, bar_height, fill=True, stroke=False)

    y -= 30

    # 3. Detalhamento por Disciplina
    canvas.set_fill_color(0.12, 0.23, 0.54)
    canvas.draw_text(40, y, "DETALHAMENTO POR DISCIPLINA", font="F2", size=12)
    y -= 15

    if not subjects:
        canvas.set_fill_color(0.5, 0.5, 0.5)
        canvas.draw_text(40, y, "Nenhuma disciplina cadastrada para este aluno.", font="F3", size=10)
    else:
        # Agrupa tarefas por subject_id
        tasks_by_subject = {}
        for t in tasks:
            s_id = t.get("subject_id")
            tasks_by_subject.setdefault(s_id, []).append(t)

        for subj in subjects:
            s_id = subj.get("id")
            s_name = subj.get("name") or "Disciplina sem nome"
            s_code = subj.get("code") or ""
            s_prof = subj.get("professor") or subj.get("teacher") or "Não informado"
            s_sem = subj.get("semester") or ""

            subj_tasks = tasks_by_subject.get(s_id, [])
            subj_total = len(subj_tasks)
            subj_completed = sum(
                1 for t in subj_tasks if str(t.get("status", "")).strip().lower() in ["concluída", "concluida", "completed", "done"]
            )
            subj_rate = round((subj_completed / subj_total * 100), 1) if subj_total > 0 else 0.0

            # Quebra de página se espaço insuficiente
            needed_space = 40 + max(len(subj_tasks), 1) * 18
            if y - needed_space < 65:
                canvas.new_page()
                current_page += 1
                draw_header_footer(current_page)
                y = 740

            # Bloco da Disciplina
            canvas.set_fill_color(0.94, 0.96, 0.99)
            canvas.rect(40, y - 22, 515, 22, fill=True, stroke=False)

            canvas.set_fill_color(0.12, 0.23, 0.54)
            code_label = f" ({s_code})" if s_code else ""
            canvas.draw_text(48, y - 15, f"• {s_name}{code_label}", font="F2", size=10)

            # Resumo da disciplina à direita
            rate_label = f"{subj_completed}/{subj_total} concluídas ({subj_rate}%)"
            canvas.set_fill_color(0.3, 0.3, 0.3)
            canvas.draw_text(400, y - 15, rate_label, font="F1", size=9)

            y -= 26

            # Linha de metadados
            canvas.set_fill_color(0.45, 0.45, 0.45)
            prof_info = f"Professor: {s_prof}"
            sem_info = f"Semestre: {s_sem}" if s_sem else ""
            meta_str = f"{prof_info}   |   {sem_info}" if sem_info else prof_info
            canvas.draw_text(52, y - 10, meta_str, font="F3", size=8.5)
            y -= 18

            # Lista de tarefas
            if not subj_tasks:
                canvas.set_fill_color(0.6, 0.6, 0.6)
                canvas.draw_text(60, y - 10, "Nenhuma tarefa vinculada a esta disciplina.", font="F3", size=8.5)
                y -= 16
            else:
                for task in subj_tasks:
                    if y < 65:
                        canvas.new_page()
                        current_page += 1
                        draw_header_footer(current_page)
                        y = 740

                    t_title = task.get("title") or "Sem título"
                    t_status = task.get("status") or "Pendente"
                    t_due = task.get("due_date") or "Sem prazo"

                    is_done = str(t_status).strip().lower() in ["concluída", "concluida", "completed", "done"]

                    # Badge de status
                    if is_done:
                        canvas.set_fill_color(0.85, 0.95, 0.88)
                        canvas.rect(58, y - 12, 60, 12, fill=True, stroke=False)
                        canvas.set_fill_color(0.10, 0.55, 0.25)
                        canvas.draw_text(62, y - 9, "[CONCLUÍDA]", font="F2", size=7.5)
                    else:
                        canvas.set_fill_color(0.98, 0.93, 0.88)
                        canvas.rect(58, y - 12, 60, 12, fill=True, stroke=False)
                        canvas.set_fill_color(0.75, 0.35, 0.10)
                        canvas.draw_text(65, y - 9, "[PENDENTE]", font="F2", size=7.5)

                    canvas.set_fill_color(0.2, 0.2, 0.2)
                    canvas.draw_text(125, y - 9, t_title[:55], font="F1", size=9)

                    canvas.set_fill_color(0.5, 0.5, 0.5)
                    canvas.draw_text(450, y - 9, f"Prazo: {t_due}", font="F1", size=8)

                    y -= 16

            y -= 10

    return canvas.output()


def generate_report_file(
    output_path: str,
    token: Optional[str] = None,
    base_url: Optional[str] = None,
    sample: bool = False
) -> Tuple[bool, str]:
    """Gera o arquivo PDF de relatório de desempenho do estudante."""
    if sample:
        data = get_sample_report_data()
    else:
        success, res = fetch_report_data(token=token, base_url=base_url)
        if not success:
            return False, res.get("error", "Erro ao obter dados do relatório.")
        data = res

    try:
        pdf_bytes = render_student_report_pdf(data)
        out_dir = os.path.dirname(os.path.abspath(output_path))
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)

        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

        return True, f"Relatório PDF gerado com sucesso em: {os.path.abspath(output_path)}"
    except Exception as e:
        return False, f"Erro ao renderizar o PDF: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="Gera relatório de desempenho acadêmico do aluno em PDF (EduTrack AI)."
    )
    parser.add_argument(
        "-o", "--output",
        default="relatorio_desempenho.pdf",
        help="Caminho do arquivo PDF de saída (padrão: relatorio_desempenho.pdf)"
    )
    parser.add_argument(
        "-t", "--token",
        default=None,
        help="Token de autenticação JWT do aluno"
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="URL base personalizada dos endpoints do Xano"
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Gera o relatório com dados de exemplo offline"
    )

    args = parser.parse_args()

    success, message = generate_report_file(
        output_path=args.output,
        token=args.token,
        base_url=args.base_url,
        sample=args.sample
    )

    if success:
        print(f"[OK] {message}")
        sys.exit(0)
    else:
        print(f"[ERRO] {message}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
