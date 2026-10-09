table user_01 {
  auth = true

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text name
    email? email
    password? password filters=min:8|minAlpha:1|minDigit:1 {
      visibility = "private"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
    {
      type : "btree|unique"
      field: [{name: "xdo.email", op: "asc"}]
    }
  ]

  guid = "AayCxPkOzF66D7CLVPME4IQ88U4"
}