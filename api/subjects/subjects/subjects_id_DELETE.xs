// Delete subject record belonging to the authenticated user
query "subjects/{subjects_id}" verb=DELETE {
  api_group = "subjects"
  auth = "user"

  input {
    int subjects_id filters=min:1 {
      description = "ID of the subject to delete"
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

    db.del subjects {
      field_name = "id"
      field_value = $input.subjects_id
    }
  }

  response = null
  guid = "ug5rMADP7Pwb86IYLc0kx1DMc68"
}

