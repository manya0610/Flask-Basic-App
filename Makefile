format:
	ruff check --select I --fix src/ tests/ scripts/
	ruff format src/ tests/ scripts/

test:
	python3 -m pytest --cov=src -s
	
test-coverage:
	python3 -m pytest --cov-report html:coverage --cov=src

db_setup:
	python3 -m scripts.db_scripts create_db create_tables

drop_db:
	python3 -m scripts.db_scripts drop_db

create_db:
	python3 -m scripts.db_scripts create_db