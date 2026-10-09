// Query all STATUS_PEDIDO records
query status_pedido verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_PEDIDO {
      return = {type: "list"}
    } as $status_pedido
  }

  response = $status_pedido
  guid = "yu6JRj5mFBLjhvySoYC8C3him6o"
}