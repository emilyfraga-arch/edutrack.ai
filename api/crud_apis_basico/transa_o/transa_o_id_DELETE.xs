// Delete TRANSAÇÃO record.
query "transa_o/{transa_o_id}" verb=DELETE {
  api_group = "CRUD_APIS_BASICO"

  input {
    int transa_o_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.transa_o_id
    }
  }

  response = null
  guid = "hOgyjlX0p_HtEUHCpYsCvu20qBU"
}