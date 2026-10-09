// Add FAQ record
query faq verb=POST {
  api_group = "CRUD_APIS_BASICO"

  input {
    dblink {
      table = "FAQ"
    }
  }

  stack {
    db.add FAQ {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $faq
  }

  response = $faq
  guid = "rG53mJxEoCfNw3WhwC8GgIfElIk"
}