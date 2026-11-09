// Update subject record belonging to the authenticated user
query "subjects/{subjects_id}" verb=PATCH {
  api_group = "subjects"
  auth = "user"

  input {
    int subjects_id filters=min:1 {
      description = "ID of the subject to update"
    }
    text name? filters=trim {
      description = "Optional updated subject name"
    }
    text code? filters=trim {
      description = "Optional updated course code"
    }
    text professor? filters=trim {
      description = "Optional updated professor name"
    }
    text semester? filters=trim {
      description = "Optional updated academic semester"
    }
  }

  stack {
    db.get subjects {
      field_name = "id"
      field_value = $input.subjects_id
    } as $subject

    precondition ($subject != null && $subject.user_id == $auth.id) {
      error_type = "notfound"
      error = "Subject not found."
    }

    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input

    db.patch subjects {
      field_name = "id"
      field_value = $input.subjects_id
      data = `$input|pick:($raw_input|keys)`|filter_null
    } as $updated_subject
  }

  response = $updated_subject
  guid = "kztrJF3xXSSou6iyZFhIDznEbh0"
}

