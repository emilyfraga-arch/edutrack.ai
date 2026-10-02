// Gerencia as disciplinas acadêmicas cadastradas pelos usuários.
table subjects {
  auth = false

  schema {
    // Identificador único da disciplina (auto-incremento)
    int id

    // Chave estrangeira referenciando o usuário autenticado na tabela user
    int user_id {
      table = "user"
      description = "ID do usuário proprietário da disciplina"
    }

    // Nome da disciplina
    text name filters=trim {
      description = "Nome da disciplina"
    }

    // Nome do professor ou instrutor
    text teacher? filters=trim {
      description = "Nome do professor ou instrutor"
    }

    // Carga horária da disciplina em horas
    int hours? {
      description = "Carga horária da disciplina em horas"
    }

    // Data e hora de criação do registro
    timestamp created_at?=now {
      description = "Data de criação do registro"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
  ]
}
