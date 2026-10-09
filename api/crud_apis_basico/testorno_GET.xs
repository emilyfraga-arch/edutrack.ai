// Query all TESTORNO records
query testorno verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query TESTORNO {
      return = {type: "list"}
    } as $testorno
  }

  response = $testorno
  guid = "ePO_VyRdD2NySwGxek_ugXRppjw"
}