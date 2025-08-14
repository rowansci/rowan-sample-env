# Sample Rowan API Environment

[![License](https://img.shields.io/github/license/rowansci/rowan-sample-env)](https://github.com/rowansci/rowan-sample-env/blob/master/LICENSE)
[![Powered by: Pixi](https://img.shields.io/badge/Powered_by-Pixi-facc15)](https://pixi.sh)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

This environment uses `pixi` and `direnv` to load a minimal environment for using the Rowan API. To use this repo, click the green `Use this template` button in the top right and it will create a copy of these files in a new repository.

For a complete development environment for building on the Rowan API, we recommend instead using [pixi-cookiecutter](https://github.com/jevandezande/pixi-cookiecutter).

## Getting started
Once `pixi` and `direnv` have been installed (see [Installation](#installation) for instructions), make a `.env` in the root directory and paste your Rowan API key into it as follows:

```sh
ROWAN_API_KEY="rowan-api-key-goes-here"
```

You will need to allow `direnv` to load the environment via `direnv allow .`. The environment should now automagically load/unload every time you cd into/out of the directory.
(If the environment does not automatically load, check to make sure you [configured direnv](#configuring-direnv) correctly)

You should now be able to run the test pka job in the `test_pka.py`.


## Installation

### Pixi
Pixi is a modern package management tool.

#### Installing pixi
```sh
curl -fsSL https://pixi.sh/install.sh | bash
```
#### Configuring Pixi

If installing other programs with `pixi` (recommended), make sure that `~/.pixi/bin`
is in your path by adding the following to your .zshrc/.bashrc/.profile
```sh
export PATH=$PATH:~/.pixi/bin
```

### Direnv
[direnv](https://pixi.sh/latest/features/environment/#using-pixi-with-direnv)
can automagically load environment variables and the pixi shell.

#### Installing direnv
```sh
pixi global install direnv
```

Warning: if installed simultaneously from multiple sources, weird errors can result.

#### Configuring direnv
Make sure that direnv is available in your shell by adding the following to your
.zshrc/.bashrc/.profile (swap zsh for the name of your shell).
```sh
eval "$(direnv hook zsh)"
```

To allow direnv to automagically load/unload environment variables, you will need to type `direnv allow .` in the directory, and it will thereafter run what is in the `.envrc` file.

(You may need to cd out and then back in for things to take effect.)
