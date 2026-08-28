// Query all ENDERECO records
query endereco verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query ENDERECO {
      return = {type: "list"}
    } as $endereco
  }

  response = $endereco
}