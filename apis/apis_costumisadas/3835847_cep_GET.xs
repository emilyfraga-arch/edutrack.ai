// Retorna o resultado (local ou recém-criado)
query Cep verb=GET {
  api_group = "Apis Costumisadas"

  input {
    text Cep? filters=trim
  }

  stack {
    // 1. Busca no banco local
    db.query CEP {
      where = $db.CEP.cep == $input.Cep
      return = {type: "single"}
    } as $CEP_local
  
    conditional {
      // 2. Se não encontrar localmente, busca no ViaCEP
      if ($CEP_local == null) {
        api.request {
          url = "https://viacep.com.br/ws/" ~ ($input.Cep|replace:"-":"") ~ "/json"
          method = "GET"
        } as $viacep
      
        conditional {
          // Se encontrou no ViaCEP e não deu erro
          if (($viacep.response.status == 200) && ($viacep.response.result|has:"erro" == false)) {
            // 3. Salva no banco local para futuras consultas
            db.add CEP {
              enforce_hidden_fields = false
              data = {
                created_at: "now"
                cep       : $input.Cep
                uf        : $viacep.response.result.uf
                cidade    : $viacep.response.result.localidade
              }
            } as $CEP_result
          }
        
          else {
            var $CEP_result {
              value = null
            }
          }
        }
      }
    
      else {
        var $CEP_result {
          value = $CEP_local
        }
      }
    }
  }

  response = $CEP_result
}