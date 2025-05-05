# Makefile

.PHONY: setup docs serve lint test clean

setup:
    scripts/setup_env.sh

docs:
    .venv/bin/mkdocs build --site-dir site

serve:
    .venv/bin/mkdocs serve

lint:
    .venv/bin/flake8 .

test:
    .venv/bin/pytest

clean:
    rm -rf site .venv
