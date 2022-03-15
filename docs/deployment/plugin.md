# Install Plugins

!!!warning
    Be careful not to mistake **`rsserpent.txt`** for `requirements.txt`.

The default template doesn't do much. In order to unleash the full power of RSSerpent, you will need to add RSSerpent plugins to the `rsserpent.txt` file.

You could clone the repository to edit `rsserpent.txt` locally, or you could just use the GitHub web interface if you are not familiar with [git](https://git-scm.com/).

Several things to note when writing `rsserpent.txt`:

- It's the same as writing `requirements.txt` for any Python project;
- Do not modify `requirements.txt`, only edit `rsserpent.txt`. GitHub Actions will be in charge of automatically updating `requirements.txt` and deploying your instance;
- By *automatically* it means every week or every time you commit changes to the repository;
- It's recommended to not specify versions so that [GitHub Actions](https://github.com/features/actions) could automatically updates them;

    ```python
    # PyPI
    rsserpent
    # Git
    rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git
    ```

- If you do need a specific version of some dependency, you could always pin its version with:

    ```python
    # PyPI
    rsserpent==0.1.4
    # Git
    rsserpent-plugin-bilibili @ git+https://github.com/RSSerpent/rsserpent-plugin-bilibili.git@0609c0bd466e5d19fbb13078d9b93e0134b8c5bd
    ```
