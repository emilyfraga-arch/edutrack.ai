// Query all PAPEL records
query papel verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
  }

  stack {
    db.query PAPEL {
      sort = {papel.id: "asc"}
      return = {type: "list"}
    } as $papel
  }

  response = $papel
  guid = "FHUCrpvd90Qb6V_bnmt_Fs5z5iI"
}