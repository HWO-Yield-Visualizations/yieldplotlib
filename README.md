<p align="center">
  <img width = 250 src="https://raw.githubusercontent.com/coreyspohn/yieldplotlib/main/docs/_static/logo.png" alt="yieldplotlib logo" />
  <br><br>
</p>

<p align="center">
  <a href="https://pypi.org/project/yieldplotlib/"><img src="https://img.shields.io/pypi/v/yieldplotlib.svg?style=flat-square&logo=pypi" alt="PyPI"/></a>
  <a href="https://yieldplotlib.readthedocs.io"><img src="https://readthedocs.org/projects/yieldplotlib/badge/?version=latest&style=flat-square" alt="Documentation Status"/></a>
  <a href="https://github.com/coreyspohn/yieldplotlib/?tab=coc-ov-file"><img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=flat-square" alt="Code of Conduct"/></a>
  <a href="https://doi.org/10.5281/zenodo.15013340"><img src="https://img.shields.io/badge/DOI-10.5281/zenodo.15013340-blue?style=flat-square" alt="DOI"></a>
</p>
<!-- <a href="https://github.com/coreyspohn/yieldplotlib/actions/workflows/ci.yml/"><img src="https://img.shields.io/github/actions/workflow/status/coreyspohn/yieldplotlib/ci.yml?branch=main&logo=github&style=flat-square" alt="CI"/></a> -->


yieldplotlib
---------------------
`yieldplotlib` is a Python library created by the Visualizations Task Group of
the Exoplanet Science Yield Working Group (ESYWG) under the HWO Project Office.
The goal of this library is to communicate the results of the Exoplanet yield codes
to the broader community in a clear and visually appealing way. The library is
designed interpret the outputs of yield codes (AYO and EXOSIMS) and produce
publication-quality plots.

Documentation
---------------------

Documentation for `yieldplotlib` is hosted on
[Read the Docs](https://yieldplotlib.readthedocs.io/en/latest/#).

Installation
---------------------

Before installing, we recommend running `yieldplotlib` in a clean conda or
virtual environment. This is done by using `venv`, `virtualenv`, `uv`, `conda`,
or a similar tool. We recommend `venv` or `conda` if you are unfamiliar with
this process which can be used as follows:

##### <u> venv </u>
```bash
python3 -m venv .venv
source .venv/bin/activate
```
That creates a new "virtual environment" in the `.venv` directory and
activates it. Now when you run `python` commands it will not be from your
system level python installation, but from the one in the `.venv`
directory. To deactivate the environment, run `deactivate` from your shell.

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

##### <u> Installing yieldplotlib </u>

`yieldplotlib` is pip installable via PyPI and the latest release version can
be installed by running:

`pip install yieldplotlib`

You can also download the development version with an editable install by
cloning the repository and running:

```
cd yieldplotlib
pip install -e .
```
For more information on yieldplotlib development, please also see the
[Developer Documentation](https://yieldplotlib.readthedocs.io/en/latest/user/dev.html).

Authors
---------------------

Corey Spohn (@CoreySpohn)

Sarah Steiger (@steigersg)
