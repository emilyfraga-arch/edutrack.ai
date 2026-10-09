// Blog table for blog posts
table blog {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }
  
    text title? filters=trim
  
    // a short description of a blog
    text description? filters=trim
  
    // contents of the blog
    text content? filters=trim
  
    text? slug?
    bool published?
    timestamp? published_at?
  
    // blog tags
    text[] tags? filters=trim
  
    int user_id? {
      table = "user_01"
    }
  
    object[] categories? {
      schema {
        text category? filters=trim
        int category_id? {
          table = "category"
        }
      }
    }
  
    image? banner?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
    {type: "btree|unique", field: [{name: "slug", op: "asc"}]}
  ]

  guid = "Xghc-4v0c__xOTokaxdP6rWrZZc"
}