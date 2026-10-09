// blog categories
table category {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text category? filters=trim
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
    {
      type : "btree|unique"
      field: [{name: "category", op: "asc"}]
    }
  ]

  guid = "ytDFkHKi9B_A7duyiuB1S-pPFno"
}