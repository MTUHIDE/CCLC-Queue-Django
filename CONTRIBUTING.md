# Contributing

## Getting Started

To get started you will want to clone the repository to your computer. Then you will want to follow the steps below.

### 1. Python

This project requires a python version of at least 3.10

### 2. Setting up Poetry

If you do not already have poetry installed you can install it [here](https://python-poetry.org/docs/master/#installing-with-the-official-installer). Going forward will assume you have installed poetry.

With poetry installed open a terminal in the project root directory and run

```shell
poetry install
```

This will have poetry create a virtual environment for you to work in with all the necessairy dependencies. Commands can be run in this virtual enviroment in two ways.

1. `poetry shell`
   * This will put you inside the virtual environment allowing you to run commands as you normally would. You can leave the virutal environment by typing `exit`
2. `poetry run <command>`
    * This will run the given command inside the virtual environment.

### 3. Setting up pre-commit hooks

You will now want to install the pre-commit hooks into your local repository. This can be done by running

```shell
poetry run pre-commit install
```

This ensures the correct checks are run when you go to make a commit.

### 4. Finished

You are now all set up and ready to develop!
