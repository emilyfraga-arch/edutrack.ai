// Get STATUS record
query "status/{status_id}" verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    int status_id? filters=min:1
  }

  stack {
    db.get STATUS {
      field_name = "id"
      field_value = $input.status_id
    } as $status
  
    precondition ($status != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $status
  guid = "xEaMfIYImBKhrFvb2FBqyW9pRys"
}