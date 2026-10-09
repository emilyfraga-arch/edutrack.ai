// Query all Colaboradores records
query colaboradores verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query Colaboradores {
      return = {type: "list"}
    } as $colaboradores
  }

  response = $colaboradores
  guid = "T4AXYTAVuuUbFhflw7X13DdVrTo"
}