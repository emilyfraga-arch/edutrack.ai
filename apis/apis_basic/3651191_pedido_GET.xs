// Query all Pedido records
query pedido verb=GET {
  api_group = "APIS_BASIC"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $pedido
  }

  response = $pedido
}