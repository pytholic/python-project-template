.PHONY: run-unit-tests
run-unit-tests:
	pytest -m unit -s --cov stringutils --cov-report=term-missing --cov-report=xml --tb=line --doctest-modules

.PHONY: run-tests
run-tests:
	pytest -s --cov stringutils --cov-report=term-missing --cov-report=xml --tb=line --doctest-modules

.PHONY: run-fast-tests
run-fast-tests:
	pytest -m "not slow" -s --cov stringutils --cov-report=term-missing --cov-report=xml --tb=line --doctest-modules
