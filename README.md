<!-- badges -->
[![Documentation](https://img.shields.io/badge/docs-latest-orange.svg)](https://master-ai-batch5.github.io/M05-mp-decaillet/index.html)
[![GitHub Project](https://img.shields.io/badge/github-project-0000c0.svg)](https://github.com/master-ai-batch5/M05-mp-decaillet)
[![PyPI Project](https://img.shields.io/badge/pypi-project-blueviolet.svg)](https://test.pypi.org/project/decm05)


# M05-mp-decaillet

Mini-project, as part of [module M05](https://moodle.fernuni.ch/course/view.php?id=3063) of [UniDistance's Master in AI](https://unidistance.ch/en/mathematics-and-computer-science/master-in-artificial-intelligence).  
- Mind the [accompanying slides](https://docs.google.com/presentation/d/1K4tIIJnhCY4eQcIWi5A6ZEol2mN5A6Cau0tL68QcjHY/edit?usp=sharing) (_access restrictions may apply_)
- Also mind this project's [documentation](https://master-ai-batch5.github.io/M05-mp-decaillet/index.html).


<!-- -------------------------------------------------- -->

## Architecture
See [doc/architecture.rst](doc/architecture.rst)

## Quick Start
See [doc/quick-start.md](doc/quick-start.md)

## Unit-tests, Coverage, Contributing
See [doc/ut-coverage-contributing.md](doc/ut-coverage-contributing.md)

## Doc

This projects uses [sphinx](https://www.sphinx-doc.org/en/master/) do generate its documentation.

### Generate sphinx doc locally
* activate your virtualenv: `workon m05-mp-decaillet`
* build doc:

#### OSX and Linux
  ```bash
  rm -rf ./doc/apidoc
  sphinx-apidoc src/ -o ./doc/apidoc --no-toc --separate --module-first
  sphinx-build doc sphinx
  ```
#### Windows

```cmd
  rmdir /S/Q ./doc/apidoc
  sphinx-apidoc src/ -o ./doc/apidoc --no-toc --separate --module-first
  sphinx-build doc sphinx
```

* open [sphinx/index.html](sphinx/index.html) in your web browser

[GitHub actions](.github/workflows/main.yml) will auto-deploy doc to [Github pages](https://master-ai-batch5.github.io/M05-mp-decaillet/)

<!-- -------------------------------------------------- -->