// Delete usuarios record.
query "usuarios/{usuarios_id}" verb=DELETE {
  api_group = "cadastro_otp"

  input {
    int usuarios_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.usuarios_id
    }
  }

  response = null
  guid = "8j_HVCvQWRpBGA7MkoBZ3-dNoyg"
}