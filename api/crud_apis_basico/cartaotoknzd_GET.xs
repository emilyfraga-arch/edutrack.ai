// Query all CARTAOTOKNZD records
query cartaotoknzd verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query CARTAOTOKNZD {
      return = {type: "list"}
    } as $cartaotoknzd
  }

  response = $cartaotoknzd
  guid = "FMzYqa2VgwX4MhorQwW8SzECpyY"
}