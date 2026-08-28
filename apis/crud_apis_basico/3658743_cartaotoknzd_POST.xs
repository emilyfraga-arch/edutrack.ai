// Add CARTAOTOKNZD record
query cartaotoknzd verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "CARTAOTOKNZD"
    }
  }

  stack {
    db.add CARTAOTOKNZD {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $cartaotoknzd
  }

  response = $cartaotoknzd
}