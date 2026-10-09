// Query all OP records
query op verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query OP {
      return = {type: "list"}
    } as $op
  }

  response = $op
  guid = "hPICBvdWV4n4Y8kwmiiyEXgMSPc"
}