query enviar verb=POST {
  api_group = "cadastro_otp"

  input {
    text email? filters=trim
  }

  stack {
    security.create_password {
      character_count = 6
      require_lowercase = false
      require_uppercase = true
      require_digit = true
      require_symbol = false
      symbol_whitelist = ""
    } as $codigo_otp
  
    var $expiracao {
      value = now|add_secs_to_timestamp:300
    }
  
    db.add users {
      enforce_hidden_fields = false
      data = {
        email         : $input.email
        otp_code      : $codigo_otp
        otp_expires_at: $expiracao
      }
    } as $users1
  
    var $pacote_email {
      value = {}|set:"OTP":$users1.otp_code
    }
  
    function.run sendgrid_dynamic_send {
      input = {
        to_email   : $input.email
        template_id: "d-6abfcec65a7c4747beaf5bf61f513f51 "
        data       : $pacote_email
      }
    } as $func2
  }

  response = $users1
  guid = "fxnecOZt2E6B1R_IgeOpiv7daws"
}