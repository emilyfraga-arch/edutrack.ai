// Query all usuarios records
query usuarios verb=GET {
  api_group = "cadastro_otp"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $usuarios
  }

  response = $usuarios
}