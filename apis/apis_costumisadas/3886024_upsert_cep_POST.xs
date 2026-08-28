// Retorna o registro criado ou atualizado
query UpsertCEP verb=POST {
  api_group = "Apis Costumisadas"

  input {
    text cep? filters=trim
    text cidade? filters=trim
    text estado? filters=trim
  }

  stack {
    // Procura se o CEP já existe na base
    db.query CEP {
      where = $db.CEP.cep == $input.cep
      return = {type: "list"}
    } as $CEP1
  
    conditional {
      // Se existir, atualiza os dados
      if ((($CEP1|count) > 0) && (($CEP1|first) cep == $input.cep)) {
        db.edit CEP {
          field_name = "id"
          field_value = ($CEP1|first).id
          enforce_hidden_fields = false
          data = {uf: $input.estado, cidade: $input.cidade}
        } as $CEP_result
      }
    
      // Caso contrário, adiciona um novo registro
      else {
        db.add CEP {
          enforce_hidden_fields = false
          data = {
            created_at: "now"
            cep       : $input.cep
            uf        : $input.estado
            cidade    : $input.cidade
          }
        } as $CEP_result
      }
    }
  }

  response = $CEP_result
}