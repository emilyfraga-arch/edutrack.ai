// Get subjects record
query "subjects/{subjects_id}" verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
    int subjects_id? filters=min:1
  }

  stack {
    db.get subjects {
      field_name = "id"
      field_value = $input.subjects_id
    } as $subjects
  
    precondition ($subjects != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $subjects
  guid = "AYmu2rTD2513XNOj4GgHdDrK_EI"
}