// Valida o código OTP enviado pelo usuário para confirmar o e-mail ou login
// Retorna os dados do usuário em caso de sucesso
query validar verb=POST {
  api_group = "cadastro_otp"

  input {
    // E-mail do usuário para buscar o registro
    text email? filters=trim
  
    // Código de verificação digitado pelo usuário
    text codigo_digitado? filters=trim
  }

  stack {
    // Verifica se o e-mail foi fornecido
    precondition ($input.email != null && $input.email != "") {
      error_type = "inputerror"
      error = "O e-mail é obrigatório."
    }
  
    // Verifica se o código foi fornecido
    precondition ($input.codigo_digitado != null && $input.codigo_digitado != "") {
      error_type = "inputerror"
      error = "O código é obrigatório."
    }
  
    // Busca o usuário pelo e-mail fornecido
    db.get users {
      field_name = "email"
      field_value = $input.email
    } as $users1
  
    // Garante que o usuário existe na base de dados
    precondition ($users1 != null) {
      error_type = "notfound"
      error = "Usuário não encontrado."
    }
  
    // Compara o código fornecido com o código armazenado no banco de dados
    precondition ($users1.otp_code == $input.codigo_digitado) {
      error_type = "inputerror"
      error = "Código de verificação inválido."
    }
  
    // Verifica se o código ainda está dentro do prazo de validade
    conditional {
      if ($users1.otp_expires_at != null) {
        precondition ($users1.otp_expires_at > now) {
          error_type = "inputerror"
          error = "O código de verificação expirou."
        }
      }
    }
  }

  response = $users1
}