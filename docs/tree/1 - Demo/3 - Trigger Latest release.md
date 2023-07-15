# Trigger ***Latest*** release workflow

## Commit message pattern

- Pattern: `\d+\.\d+\.\d+ (?i)Release.*`
- Examples ✔️:
    - 1.0.0 Release: First release.
    - 3.2.0 RELEASE
    - 5.0.2 release (foo bar)

## Example

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