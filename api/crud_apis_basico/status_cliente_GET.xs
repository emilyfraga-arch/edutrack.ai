// Query all STATUS_CLIENTE records
query status_cliente verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_CLIENTE {
      return = {type: "list"}
    } as $status_cliente
  }

  response = $status_cliente
  guid = "N5NiEscSezT7JTGs6KV1NUo9vrI"
}