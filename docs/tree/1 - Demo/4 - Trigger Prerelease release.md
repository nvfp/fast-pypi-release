# Trigger ***prerelease*** release workflow

## Commit message pattern

- Pattern: `\d+\.\d+\.\d+(b\d*)? (?i)Release.*`
- Examples ✔️:
    - 2.0.0b Release: Testing
    - 2.0.0b3 Release (dev)
    - 2.0.0b913 RELEASE: beta version
    - 1.2.3b4 release: unstable

## Example

You don’t need to set the changelog for the prerelease like you do for the latest release workflow. The GitHub prerelease description will come from the commit message.

1. Let's say your project is currently on version 1.0.0.

1. Make all the changes locally, then use `git pull` to sync with the latest remote. Now, everything is ready to be released as the `2.0.0b1` update.

1. Make a trigger commit (`git commit -am "2.0.0b1 Release: Beta version (testing)"`), then push!

The workflow will make a `2.0.0b1` git tag and a GitHub release (***prerelease***) titled `2.0.0b1` with the description `Beta version (testing)`.

> ⚠️ Note: Don't forget to pull before pushing that trigger commit, since the workflow highly depends on that commit.

The GitHub release description comes from the commit message. Note: Escape characters like `\n` are treated literally as `\` and `n`, not as a newline.