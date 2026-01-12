# Rowan Sample Environment

[![License](https://img.shields.io/github/license/rowansci/rowan-sample-env)](https://github.com/jevandezande/rowan_sample_env/blob/master/LICENSE)
[![Powered by: uv](https://img.shields.io/badge/-uv-purple)](https://docs.astral.sh/uv)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Typing: ty](https://img.shields.io/badge/typing-ty-EFC621.svg)](https://github.com/astral-sh/ty)

This environment uses `uv` and `direnv` to load a minimal environment for using the Rowan API. The environment includes `ruff` for code formatting and linting, `ty` for type checking, and `prek` for pre-commit hooks. To use this repo, click the green `Use this template` button in the top right and it will create a copy of these files in a new repository.

For a complete development environment for building on the Rowan API, we recommend instead using [uv-cookiecutter](https://github.com/jevandezande/uv-cookiecutter).

## Getting started
Once `uv` and `direnv` have been installed (see [Installation](#installation) for instructions), make a `.env` file in the root directory and paste your Rowan API key into it as follows:

```sh
ROWAN_API_KEY="rowan-api-key-goes-here"
```

You will need to allow `direnv` to load the environment via `direnv allow .`. The environment should now automagically load/unload every time you cd into/out of the directory.
(If the environment does not automatically load, check to make sure you [configured direnv](#configuring-direnv) correctly)

You should now be able to run the energy calculation in the `basic_calculation.py`.


## Installation

### Uv
[uv](https://docs.astral.sh/uv/) is a modern package management tool.

#### Installing uv
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Direnv
[direnv](https://direnv.net)
can automagically load environment variables and the uv shell.

#### Installing direnv
```sh
curl -sfL https://direnv.net/install.sh | bash
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
