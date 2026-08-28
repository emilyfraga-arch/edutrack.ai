// tABELA PEDIDO
query "pedido/{pedido_id}" verb=DELETE {
  api_group = "APIS_BASIC"

  input {
    int pedido_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.pedido_id
    }
  }

  response = null
}