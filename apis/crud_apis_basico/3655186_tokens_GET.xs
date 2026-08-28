// Query all TOKENS records
query tokens verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query TOKENS {
      return = {type: "list"}
    } as $tokens
  }

  response = $tokens
}