PYTHON = python
MANAGE = $(PYTHON) manage.py
PIP = pip

.PHONY: help migrate test dev_server prod_server install_deps

help:
	@echo "Available useful commands:"
	@echo "  make install_deps  Installs project requirements"
	@echo "  make migrate       Runs all existing migrations"
	@echo "  make test          Runs all app tests"
	@echo "  make dev_server    Starts the development server"
	@echo "  make prod_server   Starts the production server"

install_deps:
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

migrate:
	@echo "Running database migrations..."
	$(MANAGE) migrate

test:
	@echo "Running tests..."
	$(MANAGE) test parts_unlimited

dev_server:
	@echo "Starting development server..."
	$(MANAGE) runserver

prod_server:
	@echo "Starting production server..."
	gunicorn partsdanielqventus.asgi:application -k uvicorn.workers.UvicornWorker
