query atualizaEndereco verb=PATCH {
  api_group = "Apis Costumisadas"

  input {
    int cliente_id? {
      table = "CLIENTE"
    }
  
    text logradouro? filters=trim
    text numero? filters=trim
    text complemento? filters=trim
    text referencia? filters=trim
    text cep? filters=trim
    text cidade? filters=trim
    text estado? filters=trim
    bool padrao?
    int endereco_id? {
      table = "ENDERECO"
    }
  
    text bairro? filters=trim
  }

  stack {
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:WhGDeKvZ/UpsertCEP"
      method = "POST"
      params = {
        cep   : $input.cep
        cidade: $input.cidade
        uf    : $input.estado
      }
    
      headers = ["Content-Type: application/json"]
    } as $api1
  
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:FthGbjUk/endereco/" ~$input.endereco_id
      method = "PATCH"
      params = {
        endereco_id: $input.endereco_id
        cliente_id : $input.cliente_id
        logradouro : $input.logradouro
        numero     : $input.numero
        complemento: $input.complemento
        bairro     : $input.bairro
        referencia : $input.referencia
        cep_id     : $api1.response.result.id
        padrao     : $input.padrao
      }
    
      headers = ["Content-Type: application/json"]
    } as $api2
  }

  response = {
    api1                                                                                                                                                                                                                                                                                                      : $api1
    endereco_idinput_endereco_idcliente_idinput_cliente_idlogradouroinput_logradouronumeroinput_numerocomplementoinput_complementobairroinput_bairroreferenciainput_referenciacepcep_idvar_api1_response_result_idcidadevar_api1_response_result_cidadeestadovar_api1_response_result_estadopadraoinput_padrao: ```
      {
        "endereco_id": $input.endereco_id,
        "cliente_id": $input.cliente_id,
        "logradouro": $input.logradouro,
        "numero": $input.numero,
        "complemento": $input.complemento,
        "bairro": $input.bairro,
        "referencia": $input.referencia,
        "cep": {
          "cep_id": $var.api1.response.result.id,
          "cidade": $var.api1.response.result.cidade,
          "estado": $var.api1.response.result.estado
        },
        "padrao": $input.padrao
      }
      ```
  }

  guid = "kUsD8SQCBwxP0VW9p6sD-fxHt98"
}