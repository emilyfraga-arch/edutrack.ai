// Add TESTORNO record
query testorno verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "TESTORNO"
    }
  }

  stack {
    db.add TESTORNO {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $testorno
  }

  response = $testorno
}