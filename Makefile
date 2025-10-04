.PHONY: test coverage check

test:
	export PYTHONPATH=`pwd` && \
	uv run python -Wd tests/manage.py test tests --keepdb

coverage:
	export PYTHONPATH=`pwd` && \
	uv run coverage run tests/manage.py test tests --keepdb
	uv run coverage html

check:
	uv run pre-commit run --all-files
