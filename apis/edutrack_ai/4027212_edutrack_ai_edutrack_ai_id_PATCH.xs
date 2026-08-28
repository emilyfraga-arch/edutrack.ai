// Edit edutrack-ai record
query "edutrack_ai/{edutrack_ai_id}" verb=PATCH {
  api_group = "Edutrack-ai"

  input {
    int edutrack_ai_id? filters=min:1
    dblink {
      table = "edutrack-ai"
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch "edutrack-ai" {
      field_name = "id"
      field_value = $input.edutrack_ai_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $edutrack_ai
  }

  response = $edutrack_ai
}