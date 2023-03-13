# Contributing

## Commit messages convention
As a general rule, follow [this syntax](https://gist.github.com/brianclements/841ea7bffdb01346392c) for commit messages. (Emphasis on the header-line, not so much on body and footer)


## Branching strategy
As a general rule:
- avoid pushing directly to branch `dev`
- push your changes to a feature branch (named `feature/name-in-kebab-case`) and create a [pull request](https://github.com/pulls) when you're done.


**Branch `main` is for releases only**; never push directly to main, always merge from `dev`.  
In principle a (merge) commit to `main` _is_ a release.


## Linter
The python code in this project must match [autopep8](https://pypi.org/project/autopep8/) and [isort](https://pypi.org/project/isort/) linting/formatting rules.

[GitHub actions](../.github/workflows/main.yml) will enforce these rules.

### Reformat from command line
* activate your virtualenv: `workon m05-mp-decaillet`
* apply autopep8 to all local files: `autopep8 --max-line-length=120 --recursive . -aaa --in-place`
* apply isort to all local files: `isort .`

### VS-code settings
In VS-code, the linting  can be automated as follows:
- Install extension [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (which is a [recommended extensions](../.vscode/extensions.json))
- Edit your **User** Settings:
  - CMD + shift + P > "Preferences: Open User Settings (JSON)"
- Append the following to you User Settings:
  ```json
  "python.formatting.autopep8Args": [
      "--max-line-length=120"
  ],
  "[python]": {
      "editor.defaultFormatter": "ms-python.python",
      "editor.formatOnSave": true,
      "editor.codeActionsOnSave": {
          "source.organizeImports": true,
      },
  },
  ```
