// Delete STATUS record.
query "status/{status_id}" verb=DELETE {
  api_group = "STATUS_TRANSACAO"

  input {
    int status_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.status_id
    }
  }

  response = null
}