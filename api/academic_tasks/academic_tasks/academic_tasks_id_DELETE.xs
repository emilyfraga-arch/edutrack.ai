// Delete academic task record belonging to the authenticated user
query "academic_tasks/{academic_tasks_id}" verb=DELETE {
  api_group = "academic_tasks"
  auth = "user"

  input {
    int academic_tasks_id filters=min:1 {
      description = "ID of the academic task to delete"
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

    db.del academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
    }
  }

  response = null
  guid = "ZgipifLer8WycXC2x3JHTPnMun8"
}

