// Return the created customer details and auth token
// Input definition for customer registration
query cadastraCLIENTE verb=POST {
  api_group = "Apis Costumisadas"

  input {
    text nome? filters=trim
    email email? filters=trim|lower
    password senha? {
      sensitive = true
    }
  
    text celular? filters=trim
    text cpf? filters=trim
    text status? filters=trim
  }

  stack {
    // Request signup to create a new user record
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:50EO7Tkz/auth/signup"
      method = "POST"
      params = {
        name    : $input.nome
        email   : $input.email
        password: $input.senha
      }
    
      headers = ["Content-Type: application/json"]
    } as $api1
  
    // Verify if signup was successful (status 200)
    precondition ($api1.response.status == 200) {
      error = "Falha ao criar usuário: " ~ ($api1.response.result.message ?? "Erro desconhecido")
    }
  
    // Query the status ID from the status table
    db.query STATUS_CLIENTE {
      where = $db.STATUS_CLIENTE.status == $input.status
      return = {type: "list"}
    } as $STATUS_CLIENTE1
  
    // Ensure the status exists in the database
    precondition (($STATUS_CLIENTE1|count) > 0) {
      error_type = "notfound"
      error = "Status '" ~ $input.status ~ "' não encontrado."
    }
  
    // Add the customer record to the CLIENTE table
    db.add CLIENTE {
      enforce_hidden_fields = false
      data = {
        created_at       : "now"
        nome             : $input.nome
        celular          : $input.celular
        cpf              : $input.cpf
        status_cliente_id: $STATUS_CLIENTE1[0].id
        user_id          : $api1.response.result.user_id
      }
    } as $CLIENTE1
  }

  response = {
    user_id  : $api1.response.result.user_id
    cliente  : $CLIENTE1
    authToken: $api1.response.result.authToken
  }

  guid = "rgjfqPq-JWBOqp-65QJ09s_EuFc"
}