# Django GraphQL Blog

This project is a Django-based blog application with GraphQL API support.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ademic2022/graphql-blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd graphql-blog
   ```

3. Run Docker Compose to build and start the containers:

   ```bash
   docker-compose up --build
   ```

4. Access the application in your web browser at http://localhost:8000.

## API Documentation

### GraphQL Mutations

#### Create Category

```graphql
mutation createCategory {
  createCategory(name: "category1") {
    success
  }
}
```

#### Update Category

```graphql
mutation updateCategory {
  updateCategory(id: 1, name: "updated category name") {
    success
  }
}
```

#### Delete Category

```graphql
mutation deleteCategory {
  deleteCategory(id: 1) {
    success
  }
}
```

#### Create Post

```graphql
mutation createPost {
  createPost(
    title: "My first post"
    subTitle: "example test post"
    body: "my first posts with multi line body"
    categoryId: 1
  ) {
    success
  }
}
```

#### Update Post

```graphql
mutation updatePost {
  updatePost(
    id: 1
    title: "My updated first post"
    subTitle: "updated post"
    body: "my first posts tell about blogging with graghql api"
    categoryId: 2
  ) {
    success
  }
}
```

#### Delete Post

```graphql
mutation deletePost {
  deletePost(id: 1) {
    success
  }
}
```

### GraphQL Queries

#### Categories

```graphql
query categories {
  categories {
    id
    name
  }
}
```

#### Category

```graphql
query category {
  category(id: 1) {
    id
    name
  }
}
```

#### Posts

```graphql
query posts {
  posts {
    title
    category {
      id
      name
    }
    author {
      username
    }
  }
}
```

#### Post

```graphql
query post {
  post(id: 1) {
    title
    subTitle
    body
    dateCreated
    category {
      name
    }
    author {
      username
    }
  }
}
```
