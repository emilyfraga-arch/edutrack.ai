// Create a new subject
query subjects verb=POST {
  api_group = "subjects"
  auth = "user"

  input {
    text name filters=trim
    text code? filters=trim
    text professor? filters=trim
    text semester? filters=trim
  }

  stack {
    db.add "subject" {
      data = {
        user_id  : $auth.id
        name     : $input.name
        code     : $input.code
        professor: $input.professor
        semester : $input.semester
        status   : "active"
      }
    } as $new_subject
  }

  response = $new_subject
}
