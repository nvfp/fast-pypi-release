---
permalink: /changelog/
layout: main
title: Changelog
---

# Changelog

- 1.1.0 (July 8):
    - Bug fixed:
        - When parsing the latest changelog, anything inside backticks (\`\`) will be treated as a command and executed with `echo` (in jobs: 'check-changelog-file', steps: 'Parse latest changelog').
        - After moving from the job 'rewriting the VERSION in pyproject.toml' to 'publish to PyPI,' the VERSION still isn't updated. It's probably because it happened too fast?.
            - Solution I: ~~Trying to rearrange the steps by putting 'Checkout' below 'Install dependencies'.~~
            - Solution II: ~~Checkout with precise commit hash, the commit made by the 'rewrite pyproject.toml' job.~~
            - Solution III: Do manual `git pull` after Checkout (https://github.com/actions/checkout/issues/439)
    - Dependencies updates:
        - `nvfp/gh-action-simple-release`: `1.4.0` -> `1.8.0`