// Get PAPEL record
query "papel/{papel_id}" verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    int papel_id? filters=min:1
  }

  stack {
    db.get PAPEL {
      field_name = "id"
      field_value = $input.papel_id
    } as $papel
  
    precondition ($papel != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $papel
  guid = "u5L9YJZHcjXYG8Mi8Xw13C1ViBM"
}