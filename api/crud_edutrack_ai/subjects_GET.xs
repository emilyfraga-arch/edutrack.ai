// Query all subjects records
query subjects verb=GET {
  api_group = "CRUD_Edutrack-ai"

  input {
  }

  stack {
    db.query subjects {
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
  guid = "7rhq-XZvt_8cMouAxODv3d_i2mk"
}