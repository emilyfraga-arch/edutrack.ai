// blog commnets
table comments {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    int blog_id? {
      table = "blog"
    }
  
    text comment? filters=trim
    int user_id? {
      table = "user_01"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "UNllcyPxciAykFEhwGr0YIZy0SM"
}