// Add users record
query users verb=POST {
  api_group = "cadastro_otp"

  input {
    dblink {
      table = "users"
    }
  }

  stack {
    db.add users {
      enforce_hidden_fields = false
      data = {
        created_at    : "now"
        email         : $input.email
        otp_code      : $input.otp_code
        otp_expires_at: $input.otp_expires_at
      }
    } as $model
  }

  response = $model
}