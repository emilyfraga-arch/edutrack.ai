// Delete users record.
query "users/{users_id}" verb=DELETE {
  api_group = "teste"

  input {
    int users_id? filters=min:1
  }

  stack {
    db.del users {
      field_name = "id"
      field_value = $input.users_id
    }
  }

  response = null
}