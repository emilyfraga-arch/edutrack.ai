table Colaboradores {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text nome filters=trim
    text email? filters=trim
    password? password
    int papel_id {
      table = "PAPEL"
    }
  
    int status_cliente_id? {
      table = "STATUS_CLIENTE"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
    {type: "btree|unique", field: [{name: "email", op: "asc"}]}
  ]

  guid = "0YZKqdgUhkImOxZwoIj5kXYEeC0"
}