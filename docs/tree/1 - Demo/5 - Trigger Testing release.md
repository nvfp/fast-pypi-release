# Release ***Testing***

After pushing the `trigger commit`, this workflow will:
- Create a Git tag
- Publish to PyPI


## The `trigger commit` message pattern

To start the workflow, commit with the pattern below.

- Pattern: `\d+\.\d+\.\d+b\d* (?i)Testing.*`
- Examples ✔️:
    - 1.0.0b Testing
    - 5.5.5b5 TESTING: testing foo
    - 2.2.2b10 testing (dev)


## Workflow

Note: This one is the same as `Release Prerelease`. You don't need to touch the Changelog file. The Git tag note will be parsed from the commit message.

1. Finish all your work locally.
1. Pull (`git pull`) any changes from the remote (if any).
1. Make the `trigger commit` (`git commit -am "1.0.0b1 Testing: This will be the Git tag note"`) to trigger the workflow.
1. Push (`git push`) the changes.
1. Wait for the workflow to complete.
1. Pull (`git pull`) again once the workflow has updated the `pyproject.toml`.


## Demo

1. Let's say your project is currently on version 1.0.0.
1. Make all the changes locally, then use `git pull` to sync with the latest remote. Let's say you want to do a test that needs your package to be published on PyPI. In that case, you can create a beta testing version like `1.0.0b1`.
1. Make a trigger commit (`git commit -am "1.0.0b1 testing: Fixing bugs: foo bar"`), then push!

The workflow will make a `1.0.0b1` git tag with the message `Fixing bugs: foo bar`.

> ⚠️ Note: Don't forget to pull before pushing that trigger commit, since the workflow highly depends on that commit.


## Tips

- 