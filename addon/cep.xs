addon CEP {
  input {
    int CEP_id? {
      table = "CEP"
    }
  }

  stack {
    db.query CEP {
      where = $db.CEP.id == $input.CEP_id
      return = {type: "single"}
    }
  }

  guid = "kSFBYV1oKwYz7TkkO8Co8EH6rlA"
}