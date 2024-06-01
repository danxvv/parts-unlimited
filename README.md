# Parts Unlimited API

## Project Description
This is a take home coding for Qventus. The project is an API that allows all CRUD operations on a Parts table and extra task to get most common words in the description of the parts.

## Technologies Used
- Python
- Django and Django Rest Framework
- SQLite
- Docker
- Docker Compose
- Makefile

## Features
- Complete CRUD operations on Parts table
- OpenAPI documentation and HATEOAS
- Useful Makefile commands and Django commands

## Prerequisites
- Docker
- Python
- Make

## Getting Started
1. Clone the repository
```bash
git clone 
```
2. Change directory to project root
```bash
cd parts_unlimited_api
```
### Docker Way
3. Build the docker image
```bash
docker build -t parts_unlimited_api .
```
4. Run the docker container
```bash
docker run -p 8000:8000 -v $(pwd):/app parts_unlimited_api
```
### Docker Compose Way
3. Run the docker compose
```bash
docker-compose up
```
### Local Way
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Run the migrations
```bash
python manage.py migrate
```
5. Run the server
```bash
python manage.py runserver
```

## Usage
- OpenAPI documentation: http://127.0.0.1:8000/api/schema/swagger-ui/#/

## Commands
- Run tests `make test` or `python manage.py test`
- Fill with fake data `python manage.py fill_data <number_of_parts>`
- Clear the database `python manage.py clean_data`