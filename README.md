# python-template

A template repository for Python development

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![static analysis workflow](https://github.com/BioDisCo/python-template/actions/workflows/static-analysis.yaml/badge.svg)](https://github.com/BioDisCo/python-template/actions/workflows/static-analysis.yaml/)
[![test workflow](https://github.com/BioDisCo/python-template/actions/workflows/test.yaml/badge.svg)](https://github.com/BioDisCo/python-template/actions/workflows/test.yaml/)

## First Steps

0. Install `pyenv`:

   ```bash
   curl https://pyenv.run | bash
   ```

   Then install a Python interpreter in `pyenv`:

   ```bash
   pyenv install 3.12
   pyenv global 3.12
   ```

   To allow multi-version testing, install multiple versions, e.g.:

   ```bash
   pyenv install 3.12 3.11 3.10
   pyenv global 3.12 3.11 3.10
   ```

1. Install the development dependencies:

   ```bash
   pip install -r requirements-dev.txt
   ```

2. Install the pre-commit hooks:

   ```bash
   pre-commit install
   ```

3. If your IDE or editor doesn't do it for you, create virtual environment:

   ```bash
   python -m venv venv
   ```

   Then activate it (do this every time you work on the project):

   ```bash
   . venv/bin/activate
   ```

   After you're done, deactivate the virtual environment:

   ```bash
   deactivate
   ```

4. Change `pyproject.toml` to match your needs (in particular project name,
   description, keywords, authors, and maintainers).

5. Change the `multiplier` directory to your project name, write your project
   code, your tests, and your example scripts.

6. Install your package locally:

   ```bash
   pip install -e .
   ```

7. After programming, put all packages you used into the
   `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

   Then remove the local package from the file (line starts with `-e`).

8. Test your code:

   ```bash
   tox
   ```

9. Add all new files via `git add`.

10. Do a dry-run of all pre-commit checks:

    ```bash
    pre-commit run --all-files
    ```

11. Commit and push your code, then check result of GitHub actions.


## Random info

### To update a Python version

1) download, via brew (in the terminal) the version needed 
    ```
    brew install python@3.12
    ```

2) check if good version
   ```
    python --version
    ```
    or
    ```
    python3.12 --version
    ```

3) to obtain the list of the libraries inside the old environment :
    ```
    pip freeze > requirements.txt
    ```

4) To create a new environment inside VSCode 
    - first delete the old environment
    - use command line to create a new environement with the Python version needed :
      ```
      python3.12 -m venv .venv 
      ```
        where here ".venv" is the name of the environment
    - activate the environment :
      ```
      source .venv/bin/activate
      ```
    - put the "requirement.txt" file INSIDE the folder of the code and import the old librairies
      ```
      pip3 install -r requirements.txt
      ```
    - finally check if the Python version is the good one 
      ```
      python --version
      ```


### To remove some files on Git

For example : DS_Store

1) Open the terminal, and select the path and the GitHub folder

2) Check on "GitHub Desktop" if the folder is sync with GitHub (and do it previously otherwise)

3) Remove the file wanted, from Git (but no physical deletion on the PC) - here .DS_Store is the name of the file -> To change
	•	rm : commande to delete files of the Git index
	•	--cached : commande to delete files of the Git index, not on the hardisk
   ```
   git rm --cached .DS_Store
   ```

4) Confirme the deletion of the file 
   ``` 
   git status
   ```
    -> We should have a message of this kind :
    Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    .DS_Store

5) Save the modifications in Git history (change the message between "" to match the modification)
   ```
   git commit -m "Remove .DS_Store file from repository"
   ```

6) Open GitHub Desktop, and select "Fetch History"

7) Add the ".DS_Store" mention inside the ".gitignore" file


### To update a library (GitHub and also PyPi)

1) If the version in GitHub is not the one that is available locally (updated by another user) -> needs to be actualised
    -> (to set the "pull" command to "merge" the local version [if we made modifications or not], and the online one, globally (= by default))
      ```
      git config pull.rebase false --global
      ```
   Then 
   ```
   git pull 
   ```

2) To commit all & add a message 
   ```
   git commit -a -m "write the comment here"
   ```

3) Add a tag (= version, readable by PyPi)
   ```
   git tag v0.0.4 
   ```
   (here nb of the version wanted)

4) Push both (code and tags) on Git
   ```
   git push
   git push --tags
   ```

5) Remove the old version on PyPi first (won't allow to add the file on another one) (dist folder)
   ```
   rm -rf dist 
   ```

6) Construct the "environment" for PyPi
   ```
   hatch build
   ```

7) Publish on PyPi 
   ```
   hatch publish
   ```


/!\ Need to "log in" via API token (easiest way) -> settings of the account and "Create API token"
/!\ The token code will appear only ONCE, so save it somewhere /!\
It will be asked when using "hatch publish" :
    username = "__token__" (2 underscores to fill)
    password = token code given 



### To open / modify inside the folder 

It will open the whole folder in VSCode
   ```
   code .
   ```
command S to save

Pay attention of the format of the files used, if there is a format problem :
   ```
   ruff format
   ```