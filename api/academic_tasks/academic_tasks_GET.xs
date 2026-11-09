// Query academic tasks belonging to the authenticated user
query academic_tasks verb=GET {
  api_group = "academic_tasks"
  auth = "user"

  input {
    int subject_id? filters=min:1 {
      description = "Filter tasks by subject ID"
    }
    text status? filters=trim {
      description = "Filter tasks by status"
    }
  }

  stack {
    db.query academic_tasks {
      where = $db.academic_tasks.user_id == $auth.id && ($input.subject_id == null || $db.academic_tasks.subject_id == $input.subject_id) && ($input.status == null || $db.academic_tasks.status == $input.status)
      return = {type: "list"}
    } as $academic_tasks
  }

  response = $academic_tasks
  guid = "zsPhu_7hnS86dXhjYyX4B0RLj9Q"
}
