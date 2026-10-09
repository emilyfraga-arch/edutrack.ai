// Query all TTOKENIZACAO records
query ttokenizacao verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query TTOKENIZACAO {
      return = {type: "list"}
    } as $ttokenizacao
  }

  response = $ttokenizacao
  guid = "CU1NvTrE3sGT50Pjxivuzj4uvJI"
}