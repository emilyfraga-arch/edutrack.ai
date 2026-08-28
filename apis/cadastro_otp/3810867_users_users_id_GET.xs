// Get users record
query "users/{users_id}" verb=GET {
  api_group = "cadastro_otp"

  input {
    int users_id? filters=min:1
  }

  stack {
    db.get users {
      field_name = "id"
      field_value = $input.users_id
    } as $model
  
    precondition ($model != null) {
      error_type = "notfound"
      error = "Not Found"
    }
  }

  response = $model
}