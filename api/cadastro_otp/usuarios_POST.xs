// Add usuarios record
query usuarios verb=POST {
  api_group = "cadastro_otp"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $usuarios
  }

  response = $usuarios
  guid = "hLPnkBY4ui9oFewBA5vDjynPSSQ"
}