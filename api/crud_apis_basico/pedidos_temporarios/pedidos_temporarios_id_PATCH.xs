// Edit pedidos_temporarios record
query "pedidos_temporarios/{pedidos_temporarios_id}" verb=PATCH {
  api_group = "CRUD_APIS_BASICO"

  input {
    int pedidos_temporarios_id? filters=min:1
    dblink {
      table = "pedidos_temporarios"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch pedidos_temporarios {
      field_name = "id"
      field_value = $input.pedidos_temporarios_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $pedidos_temporarios
  }

  response = $pedidos_temporarios
  guid = "k-f7aEq1WlfvY6wCvvNsEFmKsRA"
}