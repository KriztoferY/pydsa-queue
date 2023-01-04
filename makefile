SOURCES = pydsa-queue

.PHONY: test format lint unittest coverage pre-commit clean
test: format lint unittest

format:
	isort $(SOURCES) tests
	black $(SOURCES) tests

lint:
	pylint $(SOURCES) tests
	mypy $(SOURCES) tests

unittest:
	pytest

coverage:
	pytest --cov=$(SOURCES) --cov-branch --cov-report=term-missing tests

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .mypy_cache .pytest_cache
	rm -rf *.egg-info
	rm -rf .tox dist site
	rm -rf coverage.xml .coverage
