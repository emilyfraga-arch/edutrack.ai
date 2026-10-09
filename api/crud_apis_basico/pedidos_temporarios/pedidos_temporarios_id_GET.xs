// Get pedidos_temporarios record
query "pedidos_temporarios/{pedidos_temporarios_id}" verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    int pedidos_temporarios_id? filters=min:1
  }

  stack {
    db.get pedidos_temporarios {
      field_name = "id"
      field_value = $input.pedidos_temporarios_id
    } as $pedidos_temporarios
  
    precondition ($pedidos_temporarios != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $pedidos_temporarios
  guid = "G-h2LOTopGv8-pFsYbimDqi8hYw"
}