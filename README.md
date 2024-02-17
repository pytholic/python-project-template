# Description

I created a simple `stringutils` library with three basic functions.

# Steps

## Create a simple library

Create a simple `stringutils` library. I included only three functions in it to keep it simple.

## Add docstrings

I added function-level and file-level strings (where necessary). For function level strings, I followed the `numpy` docstring format.

## Add requirements

I included requirements i.e. `base.txt` and `check.txt`. I added them under the `requirements` folder.

## Write tests

I added some tests for the functions to verify if they are working well. I am using `Pytest` for that.

### Note

- We can manually import our library functions for tests using `__init__.py`.
- Or we can leave it empty and use `[setup.py](http://setup.py)` to install and use the package in our test.

## Add pre-commit hooks

Next, I added `pre-commit` hooks to make sure that my code is in compliance with the best python practices.

## GitHub Workflows

We have two workflows i.e. `test.yml` to test our code and `lint.yml` to apply `pre-commit` hooks upon `push` and `pull-requests` to the `main/master` branch. I am also using `Codecov` action to upload test coverage report. Check the reference [link](https://docs.codecov.com/docs/quick-start) for more details.

## Packaging
