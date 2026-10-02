// Delete subject
query "subjects/{subject_id}" verb=DELETE {
  api_group = "subjects"
  auth = "user"

  input {
    int subject_id filters=min:1
  }

  stack {
    db.del "subject" {
      field_name = "id"
      field_value = $input.subject_id
    }
  }

  response = null
}
