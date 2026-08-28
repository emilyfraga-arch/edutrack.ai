// Delete cadastro record.
query "cadastro/{cadastro_id}" verb=DELETE {
  api_group = "teste"

  input {
    int cadastro_id? filters=min:1
  }

  stack {
    db.del cadastro {
      field_name = "id"
      field_value = $input.cadastro_id
    }
  }

  response = null
}