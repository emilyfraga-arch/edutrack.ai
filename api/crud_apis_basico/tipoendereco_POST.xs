// Add TIPOENDERECO record
query tipoendereco verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "TIPOENDERECO"
    }
  }

  stack {
    db.add TIPOENDERECO {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $tipoendereco
  }

  response = $tipoendereco
  guid = "BjJfTnezxNapBvUWI0Awsmc1-Kg"
}