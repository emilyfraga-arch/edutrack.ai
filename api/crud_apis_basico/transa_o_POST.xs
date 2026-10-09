// Add TRANSAÇÃO record
query transa_o verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $transa_o
  }

  response = $transa_o
  guid = "bTYsVPPohWyoYe7gRCZ6F_EYpGE"
}