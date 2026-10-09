// Add SOLCANCELAMENTO record
query solcancelamento verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "SOLCANCELAMENTO"
    }
  }

  stack {
    db.add SOLCANCELAMENTO {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $solcancelamento
  }

  response = $solcancelamento
  guid = "PYZA8KrXPtHUeY-VOC7352PzEdo"
}