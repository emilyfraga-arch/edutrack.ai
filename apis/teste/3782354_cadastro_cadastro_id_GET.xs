// Get cadastro record
query "cadastro/{cadastro_id}" verb=GET {
  api_group = "teste"

  input {
    int cadastro_id? filters=min:1
  }

  stack {
    db.get cadastro {
      field_name = "id"
      field_value = $input.cadastro_id
    } as $cadastro
  
    precondition ($cadastro != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $cadastro
}