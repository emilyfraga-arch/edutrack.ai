// Query all PRODUTO records
query produto verb=GET {
  api_group = "CRUD_APIS_BASICO"

  input {
    text nome? filters=trim
    text descricao? filters=trim
    text qnd_disp? filters=trim
    text precisa_produzir? filters=trim
    image? image?
    text url_image? filters=trim
    text categoria? filters=trim
    int preco?
  }

  stack {
    db.query PRODUTO {
      where = $db.PRODUTO.categoria includes $input.categoria
      sort = {produto.id: "asc"}
      return = {type: "list"}
    } as $produto
  }

  response = $produto
  guid = "HoQkR33tJA9ZwpW1vlttzzZRWo0"
}