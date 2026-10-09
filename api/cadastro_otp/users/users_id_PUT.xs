// Update users record
query "users/{users_id}" verb=PUT {
  api_group = "cadastro_otp"

  input {
    int users_id? filters=min:1
    dblink {
      table = "users"
    }
  }

  stack {
    db.edit users {
      field_name = "id"
      field_value = $input.users_id
      enforce_hidden_fields = false
      data = {
        email         : $input.email
        otp_code      : $input.otp_code
        otp_expires_at: $input.otp_expires_at
      }
    } as $model
  }

  response = $model
  guid = "5n6-DbTX0gPRDAr0Y6qagBhuz3U"
}