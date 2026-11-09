// Add subjects record
query subjects verb=POST {
  api_group = "CRUD_Edutrack-ai"

  input {
    dblink {
      table = "subjects"
    }
  }

  stack {
    db.add subjects {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $subjects
  }

  response = $subjects
  guid = "6L2V2DFvy-bdCCtTsI5g2LAZHcs"
}