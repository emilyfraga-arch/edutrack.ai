// Query all academic_tasks records
query academic_tasks verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
  }

  stack {
    db.query academic_tasks {
      return = {type: "list"}
    } as $academic_tasks
  }

  response = $academic_tasks
  guid = "dqVLuxSGyUYKnWFS7YT3yz5UJqM"
}