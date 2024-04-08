install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build


gendiff:
	poetry run gendiff

.PHONY: install test lint selfcheck check build
.PHONY: gendiff

PATH := $(PATH):./