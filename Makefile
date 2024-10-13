.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	poetry run python3 -m app.runner

install: pyproject.toml
	poetry install

clean:
	rm -rf `find . -type d -name __pycache__`

check:
	poetry run flake8 app/

runner: check run clean