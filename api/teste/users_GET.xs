// Query all users records
query users verb=GET {
  api_group = "teste"

  input {
  }

  stack {
    db.query users {
      return = {type: "list"}
    } as $users
  }

  response = $users
  guid = "JilEiZuKF67BDIFyw7AKC_AuAOo"
}