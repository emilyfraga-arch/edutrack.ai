// Add pedidos_temporarios record
query pedidos_temporarios verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "pedidos_temporarios"
    }
  }

  stack {
    db.add pedidos_temporarios {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $pedidos_temporarios
  }

  response = $pedidos_temporarios
  guid = "RbphNPZSVx9JWH48sFpQoH_GVcg"
}