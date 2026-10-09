// Query all STATUS_TTOKENIZACAO records
query status_ttokenizacao verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query STATUS_TTOKENIZACAO {
      return = {type: "list"}
    } as $status_ttokenizacao
  }

  response = $status_ttokenizacao
  guid = "LGjSvetTINaP9_F6FIdyA9YTWlA"
}