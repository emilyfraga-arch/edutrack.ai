// Query all subjects belonging to the authenticated user
query subjects verb=GET {
  api_group = "subjects"
  auth = "user"

  input {
  }

  stack {
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
  guid = "WjbFcr09jM4TNpqjbL7qdRSmZIY"
}

