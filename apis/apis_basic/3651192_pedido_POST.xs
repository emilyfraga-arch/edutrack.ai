// Add Pedido record
query pedido verb=POST {
  api_group = "APIS_BASIC"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $pedido
  }

  response = $pedido
}