run:
	uv run python manage.py runserver

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

createsuperuser:
	uv run python manage.py createsuperuser

start:
	uv run python manage.py shell;
	from cafes.models import Cafe
