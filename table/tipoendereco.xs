table TIPOENDERECO {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text tipo? filters=trim
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree|unique", field: [{name: "tipo", op: "desc"}]}
  ]

  guid = "SV7oVsp_oltEoHNh7EZgC8TMGxU"
}