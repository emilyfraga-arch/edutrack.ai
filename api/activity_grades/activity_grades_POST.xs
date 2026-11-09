// Submit a grade for a student activity
query activity_grades verb=POST {
  api_group = "activity_grades"
  auth = "user"

  input {
    int student_id filters=min:1 {
      description = "ID of the student"
    }
    int academic_task_id filters=min:1 {
      description = "ID of the evaluated academic task"
    }
    decimal grade filters=min:0 {
      description = "Score or grade awarded"
    }
    text feedback? filters=trim {
      description = "Optional feedback from professor"
    }
  }

  stack {
    db.add activity_grades {
      data = {
        user_id         : $auth.id
        student_id      : $input.student_id
        academic_task_id: $input.academic_task_id
        grade           : $input.grade
        feedback        : $input.feedback
        created_at      : "now"
      }
    } as $new_grade
  }

  response = $new_grade
  guid = "-oC_sOXo8UO8mOY5V6D5lEQj8oY"
}

