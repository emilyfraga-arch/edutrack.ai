// Stores academic subjects registered by users.
table subject {
  auth = false

  schema {
    // Unique identifier for the subject
    int id

    // ID of the student/user who owns this subject
    int user_id {
      table = "user"
      description = "ID of the student/user who owns this subject"
    }

    // Name or title of the subject
    text name filters=trim {
      description = "Name or title of the subject"
    }

    // Course or subject code (e.g. MAT101)
    text code? filters=trim {
      description = "Course or subject code (e.g. MAT101)"
    }

    // Name of the professor or instructor
    text professor? filters=trim {
      description = "Name of the professor or instructor"
    }

    // Academic term or semester (e.g. 2026.1)
    text semester? filters=trim {
      description = "Academic term or semester (e.g. 2026.1)"
    }

    // Current status of the subject
    enum status? {
      values = ["active", "completed", "archived"]
      description = "Current status of the subject"
    }

    // Timestamp when the subject was created
    timestamp created_at?=now {
      description = "Timestamp when the subject was created"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "status", op: "asc"}]}
  ]
}
