install:
	poetry install

project:
	poetry run project

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	poetry run python3 -m pip install dist/*.whl --force-reinstall

prompt:
	poetry add prompt

run:
	poetry run python -m src.primitive_db.main

lint:
	poetry run ruff check

database:
	poetry run database
