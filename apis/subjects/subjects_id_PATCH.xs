// Update subject
query "subjects/{subject_id}" verb=PATCH {
  api_group = "subjects"
  auth = "user"

  input {
    int subject_id filters=min:1
    text name? filters=trim
    text code? filters=trim
    text professor? filters=trim
    text semester? filters=trim
    enum status? {
      values = ["active", "completed", "archived"]
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input

    db.patch "subject" {
      field_name = "id"
      field_value = $input.subject_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $updated_subject
  }

  response = $updated_subject
}
