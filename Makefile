.PHONY: test coverage check

test:
	export PYTHONPATH=`pwd` && \
	python -Wd tests/manage.py test tests --keepdb

coverage:
	export PYTHONPATH=`pwd` && \
	coverage run tests/manage.py test tests --keepdb
	coverage html

check:
	pre-commit run --all-files
