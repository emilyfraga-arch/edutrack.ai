addon itemProduto {
  input {
    int item_id? {
      table = "ITEM"
    }
  }

  stack {
    db.query ITEM {
      return = {type: "list"}
    }
  }

  guid = "bv9pE0z3DMzGwUUZoFkPOyoFrbU"
}