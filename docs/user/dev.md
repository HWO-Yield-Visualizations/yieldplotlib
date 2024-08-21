# Developer Documentation

We welcome any contributions and collaboration on our development efforts, which are hosted [on GitHub](https://github.com/coreyspohn/yieldplotlib). Below are the different ways you can contribute and the steps to get involved.

## Contributing Code or Documentation

New to contributing code on GitHub? We recommend reviewing the [AstroPy
developer
documentation](https://docs.astropy.org/en/stable/development/workflow/development_workflow.html)
to get familiar with the workflow. The most important first step is to get
comfortable with the `git` version control system and the GitHub platform.
Additionally, we highly recommend making many small commits with clear commit
messages (following the Conventional Commit structure [described below](#conventional-commits-and-semantic-versioning)), as this makes it easier to
review and understand your changes.

### Setting Up Your Development Environment

#### 1. Clone the Repository:

Clone the repository to your local machine using the shell command
```bash
git clone git@github.com:HWO-Yield-Visualizations/yieldplotlib.git
```
Next, navigate to the repository directory and create a new branch:
```bash
cd yieldplotlib
git checkout -b BRANCHNAME
```
Replace `BRANCHNAME` with a descriptive name for your contribution.

#### 2. Create an Isolated Development Environment:

Python development typically uses virtual environments to isolate
dependencies for different projects, ensuring that each project has its own
specific package versions without conflicts. Set up an isolated environment
using `venv`, `virtualenv`, `uv`, `conda`, or a similar tool. We recommend `venv`
or `conda` if you are unfamiliar with this process which can be used as follows:

##### <u> venv </u>
```bash
python3 -m venv .venv
source .venv/bin/activate
```
That creates a new "virtual environment" in the `.venv` directory and
activates it. Now when you run `python` commands it will not be from your
system level python installation, but from the one in the `.venv`
directory. To deactivate the environment, run `deactivate` from your shell.

Next if using a `pip` based environment, which `venv` and `virtualenv` are,
install the developer dependencies as follows:
```bash
python -m pip install -U pip
python -m pip install -U -e ".[dev]"
```

##### <u> conda </u>

```bash
conda create -n ypl
conda activate ypl
```
Here we have named our environment `ypl`, but you can theoretically name it
whatever you like.

That creates a new "virtual environment" in the `conda/envs` directory and
activates it. Now when you run `python` commands it will not be from your
system level python installation, but from the one in the `envs/bin`
directory. To deactivate the environment, run `deactivate` from your shell.

Now install the developer dependencies as follows:
```bash
conda install pip
python -m pip install -U -e ".[dev]"
```

#### 3. Install pre-commit hooks
We use pre-commit hooks to automatically format code and check for common
errors before you commit changes. To install these hooks, run the following
commands:
```bash
pip install pre-commit
pre-commit install --hook-type commit-msg
```
This will automatically run the hooks before each commit. If any of the hooks
fail, the commit will be aborted and it will tell you what needs to be
changed. It may fix the error itself, in which case you will see a line `-
files were modified by this hook`. You can also run the hooks manually with
`pre-commit run --all-files`.

### Making Contributions

Our project is structured like a typical Python project, with the module root
in the `src/yieldplotlib` directory to prevent import issues and enforce a
clear separation between the source code and other files such as configuration,
documentation, and tests. Here are some key areas to help you get started:

#### Conventional Commits and Semantic Versioning
##### TL;DR
When making a commit (or pull request!) use a message that follows the
structure of `type(scope): message`. For example,
- `feat(plotting): add new feature X`
- `fix(plotting): fix bug Y`
- `docs(tutorials): update documentation for Z`
- `test: add test for W`
- `chore: update CI/CD configuration`
- `style(plotting): format code with ruff`
- `refactor(plotting): refactor code for readability`

In the command line, this would look like:
```bash
git add src/yieldplotlib/file_with_feat_X.py
git commit -m "feat(plotting): add new feature X"
```

##### `type`
The `type` is required and should be one of the following:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `chore`: Changes to the build process or auxiliary tools
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `ci`: Changes to our CI/CD configuration
- `build`: Changes that affect the build system or external dependencies

##### `(scope)`
The `(scope)` is optional, but should be used when the commit message is
unclear without it.

All commits must be "atomic" and thus able to be described by a singular `type`
and `scope` with few (rare) exceptions.

##### Breaking changes
If you're making a change that is incompatible with the current version (e.g.
removing a feature, changing a function call, etc), you should also include an
exclamation point at the end of the commit message, like so: `feat(plotting)!:
add new feature X` to indicate that this is a breaking change, which will
trigger a major version bump in the next release.

##### Why?
This convention allows us to quickly understand the contents of a commit and automatically generate
- The version number for the package based on [semantic versioning](https://semver.org/)
- The changelog for the package based on the commit messages
- The release notes for the package based on the commit messages
- A new distributable version of the package that is pushed to PyPI
- A new release of the package to GitHub

##### Semantic Versioning
We use [semantic versioning](https://semver.org/) to manage releases. This
means that the version number of the package is incremented based on the
type of changes made. The version number is generated by
[release-please](https://github.com/googleapis/release-please) and our
build backend [Hatch](https://hatch.pypa.io) creates a `_version.py` file
to store the version number. You never need to manually edit the version
number.

The version number is structured as `MAJOR.MINOR.PATCH`. An example of
this is `1.2.3`, where `1` is the major version, `2` is the minor version,
and `3` is the patch version.

##### Misc
If you're unsure about the type of commit, use `chore` as a catch-all
and we can help you decide the correct type.

#### Tutorials
Tutorials are written in Jupyter Notebooks. Tutorial files are located
in the `docs/tutorials` directory as `.ipynb` files. To edit these files
and run them using your virtual environment, you'll need to add the kernel
to Jupyter. To do so, run the following commands:
```bash
source .venv/bin/activate # Activate your virtual environment
pip install jupyter
pip install ipykernel
python -m ipykernel install --user --name=venv --display-name="yieldploltlib" # Add the kernel to the Jupyter server
jupyter-notebook # Start the Jupyter Notebook server
```

When contributing a new tutorial, follow the format of existing ones and
add a link to the tutorial in the `docs/index.md` file so that it is
included in the documentation site.


### Testing Your Contributions

When adding a new feature or fixing a bug, include at least one test to verify the behavior of your code. Before submitting a pull request, run all unit tests with the following command:

    python -m pytest -v tests

We appreciate your contributions and look forward to collaborating with you!
