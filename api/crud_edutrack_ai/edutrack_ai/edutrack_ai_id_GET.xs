// Get edutrack-ai record
query "edutrack_ai/{edutrack_ai_id}" verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
    int edutrack_ai_id? filters=min:1
  }

  stack {
    db.get "edutrack-ai" {
      field_name = "id"
      field_value = $input.edutrack_ai_id
    } as $edutrack_ai
  
    precondition ($edutrack_ai != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $edutrack_ai
  guid = "X-5wd9_WzoKaBY5Mk7LvMTbmMok"
}