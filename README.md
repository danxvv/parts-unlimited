# Parts Unlimited API

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Docker Way](#docker-way)
  - [Docker Compose Way](#docker-compose-way)
  - [Local Way](#local-way)
- [Usage](#usage)
  - [Endpoints](#endpoints)
    - [Common Words](#common-words)
    - [Parts](#parts)
- [Commands](#commands)

## Project Description
This project is a take-home coding challenge for Qventus. It is an API that allows all CRUD operations on a Parts table and includes an extra task to get the most common words in the description of the parts.

## Technologies Used
- Python
- Django and Django Rest Framework
- SQLite
- Docker
- Docker Compose
- Makefile

## Features
- Complete CRUD operations on the Parts table
- OpenAPI documentation and HATEOAS
- Useful Makefile commands and Django commands

## Prerequisites
- Docker
- Python
- Make

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Change directory to the project root:
   ```bash
   cd parts_unlimited_api
   ```

### Docker Way

3. Build the Docker image:
   ```bash
   docker build -t parts_unlimited_api .
   ```

4. Run the Docker container:
   ```bash
   docker run -p 8000:8000 -v $(pwd):/usr/src/app parts_unlimited_api
   ```

### Docker Compose Way

3. Run Docker Compose:
   ```bash
   docker-compose up
   ```

### Local Way

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Usage

- OpenAPI documentation: [http://127.0.0.1:8000/api/schema/swagger-ui/#/](http://127.0.0.1:8000/api/schema/swagger-ui/#/)

### Endpoints

#### Common Words

Retrieve the 5 most common words in the descriptions of all parts.

- **GET /api/common-words/**

  **Description**: Retrieve the 5 most common words in the descriptions of all parts.

  **Responses**:
  - `200`: Success

  **Response Schema**:
  ```json
  [
    {
      "word": "string",
      "count": 123
    }
  ]
  ```

#### Parts

Manage parts in the system.

- **GET /api/parts/**

  **Description**: Retrieve a list of parts, optionally filtered by `is_active`.

  **Parameters**:
  - `is_active` (query, boolean, optional): Filter parts by their active status.
  - `page` (query, integer, optional): A page number within the paginated result set.

  **Responses**:
  - `200`: Success

  **Response Schema**:
  ```json
  {
    "count": 123,
    "next": "http://api.example.org/accounts/?page=4",
    "previous": "http://api.example.org/accounts/?page=2",
    "results": [
      {
        "id": 1,
        "name": "string",
        "sku": "string",
        "description": "string",
        "weight_ounces": 123,
        "is_active": true,
        "links": [{"key": "value"}]
      }
    ]
  }
  ```

- **POST /api/parts/**

  **Description**: Create a new part.

  **Request Body** (required):
  ```json
  {
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true
  }
  ```

  **Responses**:
  - `201`: Created

  **Response Schema**:
  ```json
  {
    "id": 1,
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true,
    "links": [{"key": "value"}]
  }
  ```

- **GET /api/parts/{id}/**

  **Description**: Retrieve a single part by ID.

  **Parameters**:
  - `id` (path, integer, required): A unique integer value identifying this part.

  **Responses**:
  - `200`: Success

  **Response Schema**:
  ```json
  {
    "id": 1,
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true,
    "links": [{"key": "value"}]
  }
  ```

- **PUT /api/parts/{id}/**

  **Description**: Update an existing part.

  **Parameters**:
  - `id` (path, integer, required): A unique integer value identifying this part.

  **Request Body** (required):
  ```json
  {
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true
  }
  ```

  **Responses**:
  - `200`: Success

  **Response Schema**:
  ```json
  {
    "id": 1,
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true,
    "links": [{"key": "value"}]
  }
  ```

- **PATCH /api/parts/{id}/**

  **Description**: Partially update an existing part.

  **Parameters**:
  - `id` (path, integer, required): A unique integer value identifying this part.

  **Request Body** (required):
  ```json
  {
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true
  }
  ```

  **Responses**:
  - `200`: Success

  **Response Schema**:
  ```json
  {
    "id": 1,
    "name": "string",
    "sku": "string",
    "description": "string",
    "weight_ounces": 123,
    "is_active": true,
    "links": [{"key": "value"}]
  }
  ```

- **DELETE /api/parts/{id}/**

  **Description**: Delete an existing part.

  **Parameters**:
  - `id` (path, integer, required): A unique integer value identifying this part.

  **Responses**:
  - `204`: No response body

## Commands
- Run tests:
  ```bash
  make test
  ```

  or

  ```bash
  python manage.py test parts_unlimited
  ```

- Fill with fake data:
  ```bash
  python manage.py fill_data <number_of_parts>
  ```

- Clear the database:
  ```bash
  python manage.py clean_data
  ```