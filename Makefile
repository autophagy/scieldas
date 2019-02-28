.DEFAULT_GOAL := install

.PHONY: install
install: ## Installs the scieldas package.
	pip install -e .

.PHONY: install_testing
install_testing: ## Installs the scieldas testing packages.
	pip install -e ".[testing]"

.PHONY: black
black: ## Runs black against the codebase.
	black *.py scieldas

.PHONY: test_codestyle
test_codestyle: ## Runs PEP8 and Black codestyle testing.
	flake8 *.py scieldas
	black *.py scieldas --check
	isort -c
	mypy scieldas --ignore-missing-imports

.PHONY: test
test: ## Runs unit and codestyle tests.
	python -m unittest -v
	make test_codestyle

.PHONY: production
production: ## Runs Scieldas in production mode.
	gunicorn --config gunicorn_config.py --log-config logging.conf "scieldas:create_application()"

.PHONY: development
development: ## Runs Scieldas in development mode.
	gunicorn --reload "scieldas:create_application()"
