// Add CLIENTE record
query cliente verb=POST {
  api_group = "teste"

  input {
    dblink {
      table = "CLIENTE"
    }
  }

  stack {
    db.add CLIENTE {
      enforce_hidden_fields = false
      data = {
        created_at       : "now"
        nome             : $input.nome
        celular          : $input.celular
        cpf              : $input.cpf
        status_cliente_id: $input.status_cliente_id
        user_id          : $input.user_id
      }
    } as $model
  }

  response = $model
}