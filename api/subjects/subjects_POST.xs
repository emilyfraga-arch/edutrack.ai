// Create a new subject for the authenticated user
query subjects verb=POST {
  api_group = "subjects"
  auth = "user"

  input {
    text name filters=trim {
      description = "Name of the academic subject"
    }
    text code? filters=trim {
      description = "Course or subject code"
    }
    text professor? filters=trim {
      description = "Name of the professor or instructor"
    }
    text semester? filters=trim {
      description = "Academic semester or period"
    }
  }

  stack {
    db.add subjects {
      data = {
        user_id   : $auth.id
        name      : $input.name
        code      : $input.code
        professor : $input.professor
        semester  : $input.semester
        created_at: "now"
      }
    } as $new_subject
  }

  response = $new_subject
  guid = "rremYGI7moEgg2-kbLx8_YEDN1A"
}

