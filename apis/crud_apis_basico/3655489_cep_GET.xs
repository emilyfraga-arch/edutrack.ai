// Query all CEP records
query cep verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    text CEP? filters=trim
  }

  stack {
  }

  response = $cep
}