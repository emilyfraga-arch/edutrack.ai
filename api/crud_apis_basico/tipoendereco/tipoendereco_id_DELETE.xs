// Delete TIPOENDERECO record.
query "tipoendereco/{tipoendereco_id}" verb=DELETE {
  api_group = "CRUD_APIS_BASICO"

  input {
    int tipoendereco_id? filters=min:1
  }

  stack {
    db.del TIPOENDERECO {
      field_name = "id"
      field_value = $input.tipoendereco_id
    }
  }

  response = null
  guid = "_FLZ8ZC1vyVx26hi_5Gu0WCawzw"
}