// Query all STATUS_OE records
query status_oe verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_OE {
      return = {type: "list"}
    } as $status_oe
  }

  response = $status_oe
}