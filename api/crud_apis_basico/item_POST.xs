// Add ITEM record
query item verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "ITEM"
    }
  }

  stack {
    db.add ITEM {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $item
  }

  response = $item
  guid = "WoKmjK033-1b6B7rk6c6GcGLa-E"
}