// Add academic_tasks record
query academic_tasks verb=POST {
  api_group = "CRUD_Edutrack-ai"

  input {
    dblink {
      table = "academic_tasks"
    }
  }

  stack {
    db.add academic_tasks {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $academic_tasks
  }

  response = $academic_tasks
  guid = "EWPzvg4U-_Ec6g6Q-O5OZKfSv7g"
}