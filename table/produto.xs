// Produtos cadastrados que
// podem ser incluídos como Itens de Pedidos
// dos Cliente
table PRODUTO {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text nome? filters=trim
    text descricao? filters=trim
    text categoria? filters=trim
    text qtd_disp?="0" filters=trim
    decimal preco?
    text precisa_produzir? filters=trim
    image? imagem?
    text url_image? filters=trim
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree|unique", field: [{name: "nome", op: "desc"}]}
  ]

  guid = "_ti6lNcVTUEAUIzJYUqesU-AxSE"
}