# Core

!!!note
    Make sure you have read [Environment](environment.md) before continuing.

If you are contributing to the RSSerpent core (or any existing RSerpent plugin project), read this tutorial to understand the general workflow.

## Fork

Take the RSSerpent [core](https://github.com/RSSerpent/RSSerpent) for example:

On GitHub, navigate to the repository of the project you want to contribute. Click the *Fork* button on the top-right corner to create a replicate of the original repository owned by yourself.

!!!note
    Read GitHub's [document](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to further understand forks.

## Install

Clone your forked repository locally. In your terminal, use `cd` to enter the directory and run:

```bash
poetry install
poetry run pre-commit install -t pre-commit -t commit-msg
```

This will install project dependencies as well as [pre-commit](https://pre-commit.com/) hooks. Depending on your network connection, it may take up to several minutes to install project dependencies.

!!!note
    Read GitHub's [document](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to further understand cloning.

    It's recommended to use an SSH key (instead of password) to connect to GitHub. Read GitHub's this [document](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) on how to configure SSH keys.

## Branch

In you local repository, create a new branch by running `git checkout -b <branch name>`. Do all you work on this branch, instead of the `master` (or `main`) branch. This will keep your fork free of conflict with the original repository.

Generally we use a different branch for each pull request.

!!!note
    It's a convention to name your branch `feat/xxx` if you are working on a new feature, or `fix/xxx` if you are trying to fix a bug.

## Pull Request

After you commit changes locally, you need to push these commits to the remote GitHub repository. For the first push on any branch, run `git push -u origin <branch name>`; after that you can just run `git push` for convenience.

After pushing, open the browser, navigate to your forked repository. You will see a *Pull request* button above the list of files. Click that button to create a pull request, so that you could submit your work to the original repository. The maintainer of the original repository will then decide whether or not to accept your pull request.

!!!note
    Read GitHub's [document](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to further understand pull requests.

## Further Steps

So far this tutorial is focused on discussing the general workflow of contributing to the RSSerpent core. If you are looking for some specific problem to work on, you may:

- Skim through the list of issues/discussions, find something you are interested in, claim the issue/discussion, and then submit a pull request.
- Find a bug, create an [issue](https://github.com/RSSerpent/RSSerpent/issues) to report the bug, and then if you can, submit a pull request that will resolve this issue.
- Come up with an idea of some new feature, create a [discussion](https://github.com/RSSerpent/RSSerpent/discussions) thread to see if the maintainer will accept this feature, and then if you can and the maintainer will, submit a pull request implementing this new feature.
