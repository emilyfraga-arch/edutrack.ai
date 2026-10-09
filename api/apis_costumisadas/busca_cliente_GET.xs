// Busca os dados do cliente na tabela CLIENTE usando o token de autenticação
// Retorna os dados do cliente ou um objeto vazio
query buscaCliente verb=GET {
  api_group = "Apis Costumisadas"

  input {
    // Token de autenticação do cliente
    text authToken? filters=trim
  }

  stack {
    // Chama o endpoint auth/me do grupo Authentication para identificar o usuário
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:50EO7Tkz/auth/me"
      method = "GET"
      params = $input.authToken
      headers = "Authorization: Bearer " ~ $input.authToken, "Content-Type: application/json"
    } as $api1
  
    // Processa a resposta do serviço de autenticação
    conditional {
      if ($api1.response.status == 200) {
        // Se autenticado, busca o registro do cliente associado ao ID do usuário
        // O uso do filtro 'get' evita erros se a propriedade 'id' estiver ausente
        db.get CLIENTE {
          field_name = "user_id"
          field_value = `$var.api1.response.result.id`
        } as $CLIENTE1
      }
    
      else {
        // Se a autenticação falhar, retorna um objeto vazio
        var $CLIENTE1 {
          value = {}
        }
      }
    }
  }

  response = $CLIENTE1
  guid = "McSozEWzhgH0Qe4vzUNgyzyaG6c"
}