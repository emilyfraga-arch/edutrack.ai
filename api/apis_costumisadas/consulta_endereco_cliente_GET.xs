// Retorna a lista de endereços encontrados para o cliente autenticado
// Retorna a lista de endereços como resposta da API
query consultaEnderecoCliente verb=GET {
  api_group = "Apis Costumisadas"

  input {
    // Token de autenticação do cliente enviado no cabeçalho ou parâmetro
    text authToken? filters=trim
  }

  stack {
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:WhGDeKvZ/buscaCliente"
      method = "GET"
      params = {authToken: $input.authToken}
      headers = "Authorization: Bearer " ~ $input.authToken, "Content-Type: application/json"
    } as $api1
  
    db.query ENDERECO {
      where = `$var.api1.response.result.id` == $db.ENDERECO.cliente_id
      return = {type: "list"}
      output = [
        "id"
        "created_at"
        "logradouro"
        "numero"
        "complemento"
        "bairro"
        "referencia"
        "padrao"
        "cliente_id"
      ]
    
      addon = [
        {name: "CEP", input: {CEP_id: $output.cep_id}, as: "_cep"}
      ]
    } as $ENDERECO1
  }

  response = $ENDERECO1
  guid = "1Y7kAWwtsLxcAnlLOONM4GBieec"
}