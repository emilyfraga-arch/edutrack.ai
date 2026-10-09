// Delete Colaboradores record.
query "colaboradores/{colaboradores_id}" verb=DELETE {
  api_group = "CRUD_APIS_BASICO"

  input {
    int colaboradores_id? filters=min:1
  }

  stack {
    db.del Colaboradores {
      field_name = "id"
      field_value = $input.colaboradores_id
    }
  }

  response = null
  guid = "7bp8BByGtsf_rZME7XjRZlWo6GY"
}