// Get subject record belonging to the authenticated user
query "subjects/{subjects_id}" verb=GET {
  api_group = "subjects"
  auth = "user"

  input {
    int subjects_id filters=min:1 {
      description = "ID of the subject"
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
  }

  response = $subject
  guid = "heI9VOcc8a3w-IF_yfZae7rc01M"
}

