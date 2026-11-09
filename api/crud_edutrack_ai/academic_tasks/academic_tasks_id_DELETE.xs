// Delete academic_tasks record.
query "academic_tasks/{academic_tasks_id}" verb=DELETE {
  api_group = "CRUD_Edutrack-ai"

  input {
    int academic_tasks_id? filters=min:1
  }

  stack {
    db.del academic_tasks {
      field_name = "id"
      field_value = $input.academic_tasks_id
    }
  }

  response = null
  guid = "TeWc4U1ZR5IFEwPCjCBqODKGDII"
}