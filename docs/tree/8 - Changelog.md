# Changelog

- 1.2.0 (Jul 13):
    - Bug fixed: There's still an issue with the \`\` block getting executed, and it's because the single quotes inside `x` in `echo '$x'` ([ref](https://github.com/nvfp/now-i-can-sleep/actions/runs/5540835444/jobs/10113450912)).
        - **Solution**: So, here's what happened: The flow changed. At first, the changelog text went through GitHub step outputs. But now, only the path of the changelog file is passed through the step outputs. The changelog text is opened manually with Python. Why the change? Well, it turns out fixing the issue with `echo '$x'` and `x` with single quotes was really tough.
    - Improved loggers
- 1.1.1 (July 8):
    - Improved debugger
- 1.1.0 (July 8):
    - Fixed bugs:
        - When parsing the latest changelog, anything inside backticks (\`\`) will be treated as a command and executed with `echo` (in jobs: 'check-changelog-file', steps: 'Parse latest changelog').
        - After moving from the job 'rewriting the VERSION in pyproject.toml' to 'publish to PyPI,' the VERSION still isn't updated. It's probably because it happened too fast?.
            - Solution I: ~~Trying to rearrange the steps by putting 'Checkout' below 'Install dependencies'.~~
            - Solution II: ~~Checkout with precise commit hash, the commit made by the 'rewrite pyproject.toml' job.~~
            - Solution III: Do manual `git pull` after Checkout (https://github.com/actions/checkout/issues/439)
    - Dependencies updates:
        - `nvfp/gh-action-simple-release`: `1.4.0` -> `1.8.0`