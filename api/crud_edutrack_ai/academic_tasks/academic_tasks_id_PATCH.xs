// Edit academic_tasks record
query "academic_tasks/{academic_tasks_id}" verb=PATCH {
  api_group = "CRUD_Edutrack-ai"

  input {
    int academic_tasks_id? filters=min:1
    dblink {
      table = "academic_tasks"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $academic_tasks
  }

  response = $academic_tasks
  guid = "LuZ22RCZKFM3jcAuOz9__WVIdoU"
}