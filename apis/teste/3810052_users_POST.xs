// Add users record
query users verb=POST {
  api_group = "teste"

  input {
    dblink {
      table = "users"
    }
  }

  stack {
    db.add users {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $users
  }

  response = $users
}