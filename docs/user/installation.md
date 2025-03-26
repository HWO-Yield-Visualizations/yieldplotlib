# Installation

We recommend running `yieldplotlib` in a clean conda or
virtual environment. This is done by using `venv`, `virtualenv`, `uv`, `conda`,
or a similar tool. We recommend `venv` or `conda` if you are unfamiliar with
this process which can be used as follows:

### <u> venv </u>
```bash
python3 -m venv .venv
source .venv/bin/activate
```
That creates a new "virtual environment" in the `.venv` directory and
activates it. Now when you run `python` commands it will not be from your
system level python installation, but from the one in the `.venv`
directory. To deactivate the environment, run `deactivate` from your shell.

### <u> conda </u>

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

### <u> Installing yieldplotlib </u>

`yieldplotlib` is pip installable via PyPI and the latest release version can
be installed by running:

`pip install yieldplotlib`

See the [Developer Documentation](dev.md) for more information on how to do an editable install
of yieldplotlib.
