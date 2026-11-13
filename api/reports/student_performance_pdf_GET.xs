// Retrieve consolidated performance data of the authenticated student for report generation and download
query "reports/student_performance_pdf" verb=GET {
  api_group = "reports"
  auth = "user"

  input {
  }

  stack {
    // Get the authenticated student profile
    db.get user {
      field_name = "id"
      field_value = $auth.id
      output = ["id", "name", "email", "created_at"]
    } as $student

    precondition ($student != null) {
      error_type = "notfound"
      error = "Student profile not found."
    }

    // Get subjects enrolled by the student
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $subjects

    // Get academic tasks belonging to the student
    db.query academic_tasks {
      where = $db.academic_tasks.user_id == $auth.id
      return = {type: "list"}
    } as $academic_tasks
  }

  response = {
    student       : $student
    subjects      : $subjects
    academic_tasks: $academic_tasks
    report_title  : "EduTrack AI - Relatório de Desempenho Acadêmico"
  }
}
