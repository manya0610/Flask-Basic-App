format:
	ruff check --select I --fix src/ tests/
	ruff format src/ tests/

test:
	python3 -m pytest --cov=src -s
	
test-coverage:
	python3 -m pytest --cov-report html:coverage --cov=src

