// Add TOKENS record
query tokens verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "TOKENS"
    }
  }

  stack {
    db.add TOKENS {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $tokens
  }

  response = $tokens
  guid = "t8UtQmREB-cUHtwHDLualax2mXM"
}