// Ordens de Entrega enviados
// pelo Setor Pedidos ao Setor de Entregas
table OE {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text pedido_id? filters=trim
    text status_oe_id? filters=trim
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]
}