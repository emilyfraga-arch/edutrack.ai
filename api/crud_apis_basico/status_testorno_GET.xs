// Query all STATUS_TESTORNO records
query status_testorno verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_TESTORNO {
      return = {type: "list"}
    } as $status_testorno
  }

  response = $status_testorno
  guid = "xkmPepyxWH6tjGyRMhGhw46shAU"
}