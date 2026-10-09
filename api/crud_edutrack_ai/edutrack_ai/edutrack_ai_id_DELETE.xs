// Delete edutrack-ai record.
query "edutrack_ai/{edutrack_ai_id}" verb=DELETE {
  api_group = "CRUD_Edutrack-ai"

  input {
    int edutrack_ai_id? filters=min:1
  }

  stack {
    db.del "edutrack-ai" {
      field_name = "id"
      field_value = $input.edutrack_ai_id
    }
  }

  response = null
  guid = "TgXUx0FNZkQNAmaiqRhBZesGXgs"
}