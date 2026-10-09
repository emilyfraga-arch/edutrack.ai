// Delete users record
query "users/{users_id}" verb=DELETE {
  api_group = "cadastro_otp"

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
  guid = "4yUAv8QBf1m2N6eqQfRopC6Wpvk"
}