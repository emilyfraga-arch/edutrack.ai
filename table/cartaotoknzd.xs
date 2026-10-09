// Teste de tabela para armazenar tokens de clientes da Assas. A tabela é usada para validar a autenticidade dos tokens e associá-los aos clientes correspondentes.
// validações
table CARTAOTOKNZD {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text token? filters=trim
    text codigoclienteassas? filters=trim
    int cliente_id? {
      table = "CLIENTE"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree|unique", field: [{name: "token", op: "desc"}]}
  ]

  guid = "oVNzQkgoog7iV1k4JIkIRzMEr6E"
}