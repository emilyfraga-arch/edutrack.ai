// Query all pedidos_temporarios records
query pedidos_temporarios verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query pedidos_temporarios {
      return = {type: "list"}
    } as $pedidos_temporarios
  }

  response = $pedidos_temporarios
  guid = "CmCnqCa2Q9aG3923tdwrAH2J_Z0"
}