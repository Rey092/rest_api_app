include .env
export $(shell sed 's/=.*//' .env)
MANAGE = python src/manage.py

run:
	$(MANAGE) runserver
new-migrate:
	$(MANAGE) makemigrations
migrate:
	$(MANAGE) migrate
check:
	$(MANAGE) check
check-migrate:
	$(MANAGE) makemigrations --check --dry-run
lint:
	flake8 ./blog
shell:
	$(MANAGE) shell_plus --print-sql
createsuperuser:
	$(MANAGE) createsuperuser
freeze:
	pip freeze > requirements.txt

