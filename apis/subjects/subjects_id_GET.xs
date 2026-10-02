// Get subject by ID
query "subjects/{subject_id}" verb=GET {
  api_group = "subjects"
  auth = "user"

  input {
    int subject_id filters=min:1
  }

  stack {
    db.get "subject" {
      field_name = "id"
      field_value = $input.subject_id
    } as $subject
  }

  response = $subject
}
