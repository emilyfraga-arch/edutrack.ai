// Query all edutrack-ai records
query edutrack_ai verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
  }

  stack {
    db.query "edutrack-ai" {
      return = {type: "list"}
    } as $edutrack_ai
  }

  response = $edutrack_ai
  guid = "hKLxLxuFoEy4xUbX9yzzqAGWyx0"
}