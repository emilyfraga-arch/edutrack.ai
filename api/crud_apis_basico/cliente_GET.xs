// Query all CLIENTE records
query cliente verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query CLIENTE {
      return = {type: "list"}
    } as $cliente
  }

  response = $cliente
  guid = "pZw5LI34XdpRvJ65FjFsQkMtr5Y"
}