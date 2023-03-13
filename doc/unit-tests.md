## Unit tests and coverage
* activate your virtualenv: `workon m05-mp-decaillet`
* run unit tests: `python -m unittest discover -v`
* run unit tests and display coverage report: `coverage run --source=src -m unittest -v  &&  coverage report -m`

### CI-requirements
[GitHub actions](../.github/workflows/main.yml) will enforce unit-test coverage of 100%.