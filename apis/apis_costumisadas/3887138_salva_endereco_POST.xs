// Retorna os dados do endereço e do CEP associado
query salvaEndereco verb=POST {
  api_group = "Apis Costumisadas"

  input {
    text logradouro? filters=trim
    text numero? filters=trim
    text complemento? filters=trim
    text referencia? filters=trim
    text cep? filters=trim
    text cidade? filters=trim
    text estado? filters=trim
    bool padrao?
    int cliente_id? {
      table = "CLIENTE"
    }
  }

  stack {
    // Chama o endpoint de Upsert do CEP no mesmo grupo
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:WhGDeKvZ/UpsertCEP"
      method = "POST"
      params = {
        cep   : $input.cep
        cidade: $input.cidade
        estado: $input.estado
      }
    
      headers = ["Content-Type: application/json"]
    } as $api1
  
    // Cadastra o endereço vinculando ao CEP retornado
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:FthGbjUk/endereco"
      method = "POST"
      params = {
        logradouro : $input.logradouro
        numero     : $input.numero
        complemento: $input.complemento
        referencia : $input.referencia
        padrao     : $input.padrao
        cliente_id : $input.cliente_id
        cep_id     : $api1.response.result.id
      }
    
      headers = ["Content-Type: application/json"]
    } as $api2
  }

  response = {
    logradouro : $api2.response.result.logradouro
    numero     : $api2.response.result.numero
    complemento: $api2.response.result.complemento
    referencia : $api2.response.result.referencia
    padrao     : $api2.response.result.padrao
    cliente_id : $api2.response.result.cliente_id
    cep        : ```
      {
        cep_id: $api1.response.result.id
        cidade: $api1.response.result.cidade
        estado: $api1.response.result.uf
      }
      ```
  }
}