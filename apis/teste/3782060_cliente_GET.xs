// Query all CLIENTE records
query cliente verb=GET {
  api_group = "teste"

  input {
  }

  stack {
    db.query CLIENTE {
      return = {type: "list"}
    } as $model
  }

  response = $model
}