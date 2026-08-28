// Add ENDERECO record
query endereco verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "ENDERECO"
    }
  }

  stack {
    db.add ENDERECO {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $endereco
  }

  response = $endereco
}