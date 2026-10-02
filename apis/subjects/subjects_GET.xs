// Query all subjects for the user
query subjects verb=GET {
  api_group = "subjects"
  auth = "user"

  input {
    enum status? {
      values = ["active", "completed", "archived"]
    }
  }

  stack {
    db.query "subject" {
      where = $db.subject.user_id == $auth.id
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
}
