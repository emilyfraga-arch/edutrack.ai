// Query all users records
query users verb=GET {
  api_group = "cadastro_otp"

  input {
  }

  stack {
    db.query users {
      return = {type: "list"}
    } as $model
  }

  response = $model
  guid = "jJzXjxgnd5l7bBcyV6v7bRPpNXk"
}