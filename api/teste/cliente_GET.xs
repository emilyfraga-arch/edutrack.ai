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
  guid = "Sz7DCh3DOD7RXmcWp18Avh2R3ec"
}