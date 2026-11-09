table subjects {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text name? filters=trim
    text code? filters=trim
    text professor? filters=trim
    text semester? filters=trim
    int user_id?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "qaKcuCYBg-0FI-I7JJlM1at0x4k"
}