// Query all STATUS_ITEM records
query status_item verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_ITEM {
      return = {type: "list"}
    } as $status_item
  }

  response = $status_item
  guid = "rqGT8kBEWqR_tuR6rSmFP-L1gkQ"
}