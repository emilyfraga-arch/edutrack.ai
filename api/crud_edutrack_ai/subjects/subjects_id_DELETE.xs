// Delete subjects record.
query "subjects/{subjects_id}" verb=DELETE {
  api_group = "CRUD_Edutrack-ai"

  input {
    int subjects_id? filters=min:1
  }

  stack {
    db.del subjects {
      field_name = "id"
      field_value = $input.subjects_id
    }
  }

  response = null
  guid = "TSCBbv9LwrSResUKMPdyQcb1i4k"
}