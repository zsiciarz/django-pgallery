.PHONY: test coverage

test:
	export PYTHONPATH=`pwd` && \
	python tests/manage.py test tests --keepdb

coverage:
	export PYTHONPATH=`pwd` && \
	coverage run tests/manage.py test tests --keepdb
	coverage html
