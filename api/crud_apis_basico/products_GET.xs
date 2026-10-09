query products verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    text categoria? filters=trim
  }

  stack {
    db.query PRODUTO {
      where = $db.PRODUTO.categoria includes $input.categoria
      return = {type: "list"}
    } as $PRODUTO1
  }

  response = $PRODUTO1
  guid = "O1eyr5i5WMRHJ5a3w-Mu98b01FQ"
}