// Add edutrack-ai record
query edutrack_ai verb=POST {
  api_group = "CRUD_Edutrack-ai"

  input {
    dblink {
      table = "edutrack-ai"
    }
  }

  stack {
    db.add "edutrack-ai" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $edutrack_ai
  }

  response = $edutrack_ai
  guid = "OOLakFRfjbkjdyGA4_-p3eG5py0"
}