// Add Colaboradores record
query colaboradores verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "Colaboradores"
    }
  }

  stack {
    db.add Colaboradores {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $colaboradores
  }

  response = $colaboradores
}