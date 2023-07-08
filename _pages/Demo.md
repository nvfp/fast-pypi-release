---
permalink: /demo/
layout: main
title: Demo
---

## Changelog file name format

Pattern: `.*(?i)changelog.*`

Explanation: The name can be anything, but it should at least include the word 'changelog' (not case-sensitive).

Examples ✔️:
- changelog
- CHANGELOG
- CHANGELOG.md
- CHANGELOG.txt
- Changelog.txt
- 123 - Changelog.md
- 123 - Changelog - Foo.md

## Changelog file content format

The pattern:
```txt
- \d+\.\d+\.\d+.*
- \d+\.\d+\.\d+.*
- \d+\.\d+\.\d+.*
```

If you're not familiar with the pattern above, it looks like this: `X.X.X` stands for the version and `*` means anything else:
```txt
- X.X.X*
- X.X.X*
- X.X.X*
```

Explanation: Each changelog entry should start with a hyphen (-) and be arranged from newest to oldest.

Examples I ✔️:
```txt
- 2.0.0
    - Fixed bugs:
        - Foo
        - Bar
- 1.0.0
    - First release
```

Examples II ✔️:
```txt
# Changelog

- 2.0.0 (July 3):
    - Fixed bugs:
        - Foo
        - Bar
- 1.0.0 (July 1):
    - First release
```

## Demo

1. Let's say your project is currently on version 1.0.0; The Changelog file:

    ```txt
    - 1.0.0
        - First release
    ```

1. You make updates, do all the work locally, and finish with version 2.0.0.

1. Now, update the Changelog file:

    ```txt
    - 2.0.0
        - Foo bar
    - 1.0.0
        - First release
    ```

1. Make a trigger commit (`git commit -am "2.0.0 Release"`), then push!

> ⚠️ Note: Don't forget to pull before pushing that trigger commit, since the workflow highly depends on that commit.