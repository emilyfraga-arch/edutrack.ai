// Get academic task record belonging to the authenticated user
query "academic_tasks/{academic_tasks_id}" verb=GET {
  api_group = "academic_tasks"
  auth = "user"

  input {
    int academic_tasks_id filters=min:1 {
      description = "ID of the academic task"
    }
  }

  stack {
    db.get academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
    } as $academic_task

    precondition ($academic_task != null && $academic_task.user_id == $auth.id) {
      error_type = "notfound"
      error = "Academic task not found."
    }
  }

  response = $academic_task
  guid = "23touLvKfZoJMOeyGq385LTNMS4"
}

