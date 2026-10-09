// Query all STATUS records
query status verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS {
      return = {type: "list"}
    } as $status
  }

  response = $status
  guid = "8_LQhgzH6CZOil_GX59raT46Nq4"
}