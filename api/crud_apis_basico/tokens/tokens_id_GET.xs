// Get TOKENS record
query "tokens/{tokens_id}" verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    int tokens_id? filters=min:1
  }

  stack {
    db.get TOKENS {
      field_name = "id"
      field_value = $input.tokens_id
    } as $tokens
  
    precondition ($tokens != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $tokens
  guid = "0XR4ygBRNfn5veDklu6xgfs-8Yo"
}