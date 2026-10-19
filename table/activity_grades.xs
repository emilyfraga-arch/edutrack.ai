// Stores student grades for academic tasks evaluated by professors
table activity_grades {
  auth = false

  schema {
    int id {
      description = "Unique identifier for the activity grade"
    }

    // Professor/evaluator ID
    int user_id {
      table = "user"
      description = "ID of the professor/evaluator who assigned the grade"
    }

    // Student ID
    int student_id {
      table = "user"
      description = "ID of the student who received the grade"
    }

    // Academic task ID
    int academic_task_id {
      description = "ID of the evaluated academic task"
    }

    // Grade score
    decimal grade filters=min:0 {
      description = "Score or grade awarded for the activity"
    }

    // Optional feedback
    text feedback? filters=trim {
      description = "Optional feedback or observations from the professor"
    }

    timestamp created_at?=now {
      description = "Timestamp when the grade was submitted"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "academic_task_id", op: "asc"}, {name: "student_id", op: "asc"}]}
  ]
}

