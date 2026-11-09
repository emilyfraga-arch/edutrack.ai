// Update academic task record belonging to the authenticated user
query "academic_tasks/{academic_tasks_id}" verb=PATCH {
  api_group = "academic_tasks"
  auth = "user"

  input {
    int academic_tasks_id filters=min:1 {
      description = "ID of the academic task to update"
    }
    text title? filters=trim {
      description = "Optional updated title"
    }
    text description? filters=trim {
      description = "Optional updated description"
    }
    text due_date? filters=trim {
      description = "Optional updated due date"
    }
    text status? filters=trim {
      description = "Optional updated status"
    }
    int subject_id? filters=min:1 {
      description = "Optional updated subject ID"
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

    conditional {
      if ($input.subject_id != null) {
        db.get subjects {
          field_name = "id"
          field_value = $input.subject_id
        } as $subject

        precondition ($subject != null && $subject.user_id == $auth.id) {
          error_type = "notfound"
          error = "Subject not found."
        }
      }
    }

    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input

    db.patch academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
      data = `$input|pick:($raw_input|keys)`|filter_null
    } as $updated_task
  }

  response = $updated_task
}
