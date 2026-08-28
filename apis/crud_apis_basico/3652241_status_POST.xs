// Add STATUS record
query status verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "STATUS"
    }
  }

  stack {
    db.add STATUS {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $status
  }

  response = $status
}