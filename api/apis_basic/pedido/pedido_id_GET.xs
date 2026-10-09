// Get Pedido record
query "pedido/{pedido_id}" verb=GET {
  api_group = "APIS_BASIC"

  input {
    int pedido_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.pedido_id
    } as $pedido
  
    precondition ($pedido != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $pedido
  guid = "vUnfCKinQWp5BjzVBs1s5M-E-Bw"
}