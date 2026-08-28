// Query all ITEM records
query item verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    text nome? filters=trim
    int produto_id? {
      table = "PRODUTO"
    }
  }

  stack {
    db.query ITEM {
      where = $db.ITEM.id == $input.produto_id
      return = {type: "list"}
    } as $item
  }

  response = $item
}