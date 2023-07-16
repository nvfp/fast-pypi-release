# Release ***Latest***

After pushing the `trigger commit`, this workflow will:
- Create a Git tag
- Create a GitHub release (marked as `Latest`)
- Publish to PyPI


## The `trigger commit` message pattern

To start the workflow, commit with the pattern below.

- Pattern: `\d+\.\d+\.\d+ (?i)Release.*`
- Examples ✔️:
    - 1.0.0 Release: First release.
    - 3.2.0 RELEASE
    - 5.0.2 release (foo bar)


## Workflow

1. Finish all your work locally.
1. Pull (`git pull`) any changes from the remote (if any).
1. Update the Changelog file (let's say it's for the `3.0.0` release).
1. Make the `trigger commit` (`git commit -am "3.0.0 Release"`) to trigger the workflow.
1. Push (`git push`) the changes.
1. Wait for the workflow to complete.
1. Pull (`git pull`) again once the workflow has updated the `pyproject.toml`.


## Demo

1. Let's say your project is currently on version 1.0.0; The Changelog file:

    ```txt
    - 1.0.0
        - First release
    ```

1. Make all the changes locally, then use `git pull` to sync with the latest remote. Now, everything is ready to be released as the `2.0.0` update. Remember, don’t make a trigger commit yet because we need to update the changelog file first.

1. Now, update the Changelog file:

    ```txt
    - 2.0.0
        - Foo bar
    - 1.0.0
        - First release
    ```

1. Make a trigger commit (`git commit -am "2.0.0 Release"`), then push!

The workflow will make a `2.0.0` git tag and a GitHub release titled `2.0.0` with the description `- 2.0.0\n - Foo bar`. Don't worry, the newline character will be treated as a newline.

> ⚠️ Note: Don't forget to pull before pushing that trigger commit, since the workflow highly depends on that commit.


## Tips

- Make sure the version in the trigger commit matches the version in the latest changelog in the changelog file.