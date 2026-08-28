// Mantêm as API KEYs de serviços externos, tais como SendGrid e Assas
table TOKENS {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text plataforma? filters=trim
    int token?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]
}