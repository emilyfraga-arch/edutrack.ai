// Delete pedidos_temporarios record.
query "pedidos_temporarios/{pedidos_temporarios_id}" verb=DELETE {
  api_group = "CRUD_APIS_BASICO"

  input {
    int pedidos_temporarios_id? filters=min:1
  }

  stack {
    db.del pedidos_temporarios {
      field_name = "id"
      field_value = $input.pedidos_temporarios_id
    }
  }

  response = null
  guid = "09wmgt8u8IXWAM8_JEsqs1M46x4"
}