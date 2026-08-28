// Query all TIPOENDERECO records
query tipoendereco verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query TIPOENDERECO {
      return = {type: "list"}
    } as $tipoendereco
  }

  response = $tipoendereco
}