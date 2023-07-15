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