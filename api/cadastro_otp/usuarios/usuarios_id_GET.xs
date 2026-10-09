// Get usuarios record
query "usuarios/{usuarios_id}" verb=GET {
  api_group = "cadastro_otp"

  input {
    int usuarios_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.usuarios_id
    } as $usuarios
  
    precondition ($usuarios != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $usuarios
  guid = "zYRm-WsPR9EMkCMFwaggiWD9T0I"
}