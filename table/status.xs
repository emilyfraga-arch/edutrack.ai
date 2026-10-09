// Status possíveis para
// transações envolvendo pagamentos com
// cartões de crédito
table STATUS {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text status? filters=trim
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]

  guid = "3OvqaaceXJ0V9tNqoED50zsmxCI"
}