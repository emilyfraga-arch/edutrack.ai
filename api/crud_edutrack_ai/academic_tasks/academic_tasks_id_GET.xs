// Get academic_tasks record
query "academic_tasks/{academic_tasks_id}" verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
    int academic_tasks_id? filters=min:1
  }

  stack {
    db.get academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
    } as $academic_tasks
  
    precondition ($academic_tasks != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $academic_tasks
  guid = "6U0I4G5fcBWbHDmXVbUrqFx0NbA"
}