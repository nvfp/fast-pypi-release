# Release ***Prerelease***

After pushing the `trigger commit`, this workflow will:
- Create a Git tag
- Create a GitHub release (marked as `Pre-release`)
- Publish to PyPI


## The `trigger commit` message pattern

To start the workflow, commit with the pattern below.

- Pattern: `\d+\.\d+\.\d+(b\d*)? (?i)Release.*`
- Examples ✔️:
    - 2.0.0b Release: Testing
    - 2.0.0b3 Release (dev)
    - 2.0.0b913 RELEASE: beta version
    - 1.2.3b0 release (test-ver: unstable)


## Workflow

Note: Unlike `Release Latest`, which needs you to set the Changelog to get the release description, `Release Prerelease` doesn't need you to touch the Changelog file. You can specify the release description directly from the commit message, meaning that the release description on GitHub will be parsed from the commit message.

1. Finish all your work locally.
1. Pull (`git pull`) any changes from the remote (if any).
1. Make the `trigger commit` (`git commit -am "1.0.0b1 Release: This will be the release description"`) to trigger the workflow.
1. Push (`git push`) the changes.
1. Wait for the workflow to complete.
1. Pull (`git pull`) again once the workflow has updated the `pyproject.toml`.


## Demo

1. Let's say your project is currently on version 1.0.0.
1. Make all the changes locally, then use `git pull` to sync with the latest remote. Now, everything is ready to be released as the `1.0.0b1` update.
1. Make a trigger commit (`git commit -am "1.0.0b1 Release: Beta version (testing)"`), then push!

The workflow will make a `1.0.0b1` git tag and a GitHub release (marked as `Pre-release`) titled `1.0.0b1` with the description `Beta version (testing)`.

> ⚠️ Note: Don't forget to pull before pushing that trigger commit, since the workflow highly depends on that commit.

Note: The GitHub release description comes from the commit message.
Note: if you use escape characters like `\n` in the commit message, they will be treated literally as `\` and `n`, **not** as a newline.


## Tips

- 