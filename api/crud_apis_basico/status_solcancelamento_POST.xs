// Add STATUS_SOLCANCELAMENTO record
query status_solcancelamento verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "STATUS_SOLCANCELAMENTO"
    }
  }

  stack {
    db.add STATUS_SOLCANCELAMENTO {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $status_solcancelamento
  }

  response = $status_solcancelamento
  guid = "3yKfxeqx8Gxc-r2Om7hx1pgHRx0"
}