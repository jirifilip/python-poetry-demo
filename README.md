# python-poetry-demo
Demonstration for why to use poetry with Python instead of just using .venv


## TODO:

pip:
- [ ] `pip install` installs transitive dependencies
- [ ] `pip freeze` prints all dependency versions
- [ ] `pip uninstall` does not remove transitive dependencies?
  - looks like you can use pip-autoremove but that is just too much of a hassle
- [ ] manually managing the virtual environment, manually activating it
- [ ] hard to specify main, test, research dependencies. 
  - can be done with requirements-dev.txt, requirements-research.txt but is really cumbersome
- [ ] for example, should there be one "requirements.txt" file with user-defined dependencies and one "requirements.freeze.txt" for reproducible .venv?

poetry:
- [ ] functions a lot like npm for Javascript projects
- [ ] easily support src layout
- [ ] pyproject.toml functions as a friendly "main" dependency definition
- [ ] keeps poetry.lock for reproducibility of environment
  - [ ] poetry keeps there transitive dependencies
  - [ ] automatically removes them when the "main" dependency is removed from pyproject.toml
- [ ] automatically manages creation of virtual environments, be in directly in project or in AppData (or unix equivalent)
  - automatically activates the environment on entering the project directory
- [ ] allows dependency groups (e.g. main, test, research)
  - i.e. don't have to install test or research dependencies in production
- [ ] is capable of exporting dependencies to requirements.txt, e.g. if not wanting to use poetry in production container
- [ ] lot more version constraint specifiers
- [ ] easily release libraries to Artifactory with it

tool independent:
- [ ] why use src package structure 
  - https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
  - the package manager "editable installs" the code
    - when we run tests, we are using same "version" of the package as if it were installed by our users
    - we are not treating it in any special way, e.g. by having PYTHONPATH setup in a different way than when the package is installed 
  - but "src" itself must not be part of the import path!
- [ ] prepare basic pre-commit hooks to use, basic settings, probably jupytext for keeping research
