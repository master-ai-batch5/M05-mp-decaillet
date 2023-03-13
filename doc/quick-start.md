# Quick Start
<!-- -------------------------------------------------- -->

From command line:

1. start your [virtual environment](###setup-virtual-environment): `workon m05-mp-decaillet`
2. run [main.py](main.py): `python main.py`
   - for additional options, run `python main.py --help`

<!-- -------------------------------------------------- -->

## Installation

### Setup virtual environment

This quick-start.md assumes a functional Python development environment with:

- [virtual environments](https://docs.python.org/3/library/venv.html)
- a virtualenv wrapper:
  - **OSX and Linux**: use package [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
  - **Windows**: use package [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/)

The project requires **Python 3.11.1**.

Create the virtualenv as follows:

#### OSX and Linux

```bash
rmvirtualenv m05-mp-decaillet
mkvirtualenv m05-mp-decaillet --python=/usr/local/bin/python3.11 -r requirements.txt
```

_NB: exact path to **python3.11** may vary; locate it with: `which python3.11`_

#### Windows

```cmd
rmvirtualenv m05-mp-decaillet
mkvirtualenv m05-mp-decaillet --python "%userprofile%\AppData\Local\Programs\Python\Python311\python.exe" -r requirements.txt 
```

_NB: exact path to **python3.11** may vary; locate it with: `where python` (Windows CMD) or `get-command python` (Windows PowerShell)_