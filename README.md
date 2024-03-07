# Description

A python template project following modern practices. We will work with a simple `stringutils` library with three basic functions.

# Steps

## Create a simple library

Create a simple `stringutils` library. I included only three functions in it to keep it simple.

## Add docstrings

I added function-level and file-level strings (where necessary). For function level strings, I followed the `numpy` docstring format.

## Add requirements

I included requirements i.e. `base.txt` and `check.txt`. I added them under the `requirements` folder.

## Write tests

I added some tests for the functions to verify if they are working well. I am using `Pytest` for that.

```
pytest --cov stringutils --cov-report=term-missing --tb=line
pytest --cov . --cov-report=xml --tb=line
```

### Note

- We can manually import our library functions for tests using `__init__.py`.
- Or we can leave it empty and use `[setup.py](http://setup.py)` to install and use the package in our test.

## Add pre-commit hooks

Next, I added `pre-commit` hooks to make sure that my code is in compliance with the best python practices.

```
pip install pre-commit
pre-commit install
```

It will work with each commit. To run manually:

```
pre-commit run --all-files
```

## GitHub Workflows

We have two workflows i.e. `test.yml` to test our code and `lint.yml` to apply `pre-commit` hooks upon `push` and `pull-requests` to the `main/master` branch. I am also using `Codecov` action to upload test coverage report. Check the reference [link](https://docs.codecov.com/docs/quick-start) for more details.

## Packaging

- Create `setup.py`.

  - **Note:** If you face issues with `requirements` paths, create a `MANIFEST.in` file like mine.

- Create account on pypi, build and upload.

  - Create `~HOME/pypirc` file and add credentials in it:

  ```
  [pypi]
    username = __token__
    password = <api-token>

  ```

  - Build the package.

  ```
  pip install build
  python -m build

  ```

  - Upload the package.

  ```
  twine check dist/*
  twine upload dist/*
  ```
