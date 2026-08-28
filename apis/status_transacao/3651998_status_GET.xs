// Query all STATUS records
query status verb=GET {
  api_group = "STATUS_TRANSACAO"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $status
  }

  response = $status
}