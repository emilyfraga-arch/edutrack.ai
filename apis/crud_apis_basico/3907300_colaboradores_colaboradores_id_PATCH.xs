// Edit Colaboradores record
query "colaboradores/{colaboradores_id}" verb=PATCH {
  api_group = "CRUD_APIS_BASICO"

  input {
    int colaboradores_id? filters=min:1
    dblink {
      table = "Colaboradores"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch Colaboradores {
      field_name = "id"
      field_value = $input.colaboradores_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $colaboradores
  }

  response = $colaboradores
}