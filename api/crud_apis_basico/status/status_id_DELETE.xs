// Delete STATUS record.
query "status/{status_id}" verb=DELETE {
  api_group = "CRUD_APIS_BASICO"

  input {
    int status_id? filters=min:1
  }

  stack {
    db.del STATUS {
      field_name = "id"
      field_value = $input.status_id
    }
  }

  response = null
  guid = "Zy4c2rH68ItO60Be95p7-IM0WNY"
}