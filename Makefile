setup: install lint build publish package-install

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl 

.PHONY: install test lint selfcheck check build

run_json:
	poetry run gendiff data/file1.json data/file2.json

run_yaml:
	poetry run gendiff data/file1.yaml data/file2.yaml