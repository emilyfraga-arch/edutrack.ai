// Create a new academic task for the authenticated user
query academic_tasks verb=POST {
  api_group = "academic_tasks"
  auth = "user"

  input {
    text title filters=trim {
      description = "Title of the academic task"
    }
    text description? filters=trim {
      description = "Detailed description of the task"
    }
    text due_date? filters=trim {
      description = "Due date for the task"
    }
    text status?="Pendente" filters=trim {
      description = "Current status of the task"
    }
    int subject_id filters=min:1 {
      description = "ID of the associated subject"
    }
  }

  stack {
    db.get subjects {
      field_name = "id"
      field_value = $input.subject_id
    } as $subject

    precondition ($subject != null && $subject.user_id == $auth.id) {
      error_type = "notfound"
      error = "Subject not found."
    }

    db.add academic_tasks {
      data = {
        user_id    : $auth.id
        subject_id : $input.subject_id
        title      : $input.title
        description: $input.description
        due_date   : $input.due_date
        status     : $input.status
      }
    } as $new_task
  }

  response = $new_task
  guid = "RTObRocfFJP6PPVDQHtx0jEKK5M"
}
