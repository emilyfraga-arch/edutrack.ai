// Add cadastro record
query cadastro verb=POST {
  api_group = "teste"

  input {
    dblink {
      table = "cadastro"
    }
  }

  stack {
    db.add cadastro {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $cadastro
  }

  response = $cadastro
}