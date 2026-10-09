// Get Colaboradores record
query "colaboradores/{colaboradores_id}" verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    int colaboradores_id? filters=min:1
  }

  stack {
    db.get Colaboradores {
      field_name = "id"
      field_value = $input.colaboradores_id
    } as $colaboradores
  
    precondition ($colaboradores != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $colaboradores
  guid = "FDLqP6YM_WGhkwrBbKLUOKnu8_8"
}