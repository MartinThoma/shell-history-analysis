maint:
	pip install -r requirements/dev.txt
	pre-commit autoupdate && pre-commit run --all-files
	pip-compile -U setup.py
	pip-compile -U requirements/ci.in
	pip-compile -U requirements/dev.in

upload:
	make clean
	python setup.py sdist bdist_wheel && twine upload -s dist/*
clean:
	python setup.py clean --all
	pyclean .
	rm -rf *.pyc __pycache__ build dist shell_history_analysis.egg-info shell_history_analysis/__pycache__ tests/__pycache__ tests/reports docs/build .pytest_cache .tox .coverage
