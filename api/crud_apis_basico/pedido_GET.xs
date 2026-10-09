// Query all PEDIDO records
query pedido verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query PEDIDO {
      return = {type: "list"}
    } as $pedido
  }

  response = $pedido
  guid = "6ppAt79EY3gHABrZ_5LIIY7ed6o"
}