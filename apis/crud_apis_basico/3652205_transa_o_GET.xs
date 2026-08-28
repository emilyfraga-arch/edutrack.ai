// Query all TRANSAÇÃO records
query transa_o verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $transa_o
  }

  response = $transa_o
}