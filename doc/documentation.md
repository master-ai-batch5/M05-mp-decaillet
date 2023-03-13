## Documentation

This projects uses [sphinx](https://www.sphinx-doc.org/en/master/) do generate its documentation.

### Generate sphinx doc locally
* activate your virtualenv: `workon m05-mp-decaillet`
* remove previously auto-generated doc (if any):
  - on OSX and Linux: `rm -rf ./doc/apidoc`
  - on windows: `rmdir /S/Q ./doc/apidoc`
* build doc:
  ```bash
  sphinx-apidoc src/ -o ./doc/apidoc --no-toc --separate --module-first
  sphinx-build doc sphinx
  ```

* open [sphinx/index.html](sphinx/index.html) in your web browser

### Deployment to github pages

On branch `main`, [GitHub actions](.github/workflows/main.yml) will auto-deploy doc to [Github pages](https://master-ai-batch5.github.io/M05-mp-decaillet/) (docs on other branches is not deployed - merge
On branch `main`, [GitHub actions](.github/workflows/main.yml) will auto-deploy doc to [Github pages](https://master-ai-batch5.github.io/M05-mp-decaillet/) (docs from other branches are not deployed until merged to `main` - see [contributing](ut-coverage-contributing.md))
