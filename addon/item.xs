addon item {
  input {
    int produto_id? {
      table = "PRODUTO"
    }
  }

  stack {
    db.query ITEM {
      where = $db.ITEM.id == $input.produto_id
      return = {type: "list"}
    }
  }

  guid = "pfgyLAEVZHSbRZb9HqDZKndr67E"
}