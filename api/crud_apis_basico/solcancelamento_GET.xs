// Query all SOLCANCELAMENTO records
query solcancelamento verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query SOLCANCELAMENTO {
      return = {type: "list"}
    } as $solcancelamento
  }

  response = $solcancelamento
  guid = "yE0j60NhVEDZvP07q6Tae6oTDH0"
}