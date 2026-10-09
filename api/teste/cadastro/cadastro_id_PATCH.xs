// Edit cadastro record
query "cadastro/{cadastro_id}" verb=PATCH {
  api_group = "teste"

  input {
    int cadastro_id? filters=min:1
    dblink {
      table = "cadastro"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch cadastro {
      field_name = "id"
      field_value = $input.cadastro_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $cadastro
  }

  response = $cadastro
  guid = "9rBfSv3HcTX2o69DPbAnSUoSF30"
}