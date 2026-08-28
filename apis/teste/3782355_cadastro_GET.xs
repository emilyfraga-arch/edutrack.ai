// Query all cadastro records
query cadastro verb=GET {
  api_group = "teste"

  input {
  }

  stack {
    db.query cadastro {
      return = {type: "list"}
    } as $cadastro
  }

  response = $cadastro
}