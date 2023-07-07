# Fast PyPI Release

Create GitHub release and publish to PyPI altogether within a single commit push.


## Installation

1. Copy `fast-pypi-release.yml` and put it under your repository's `.github/workflows` folder
2. Update your Git name and email by searching "EDITME" in `fast-pypi-release.yml` file
3. Make sure you have just one changelog file in the `docs` folder:
    - The file can be any extension like .txt or .md
    - The file's name should include the word "changelog" (case insensitive)
    - Visit [this page](https://nvfp.github.io/fast-pypi-release/demo) to see the allowed format of the changelog
    - The `docs` folder is at the root of your repository
4. Set up your `PYPI_USERNAME` and `PYPI_PASSWORD` as secrets in your repository's GitHub Actions (to be used by Twine for publishing to PyPI):
    1. Visit https://github.com/YOUR_USERNAME/REPOSITORY/settings/secrets/actions
    2. Create `PYPI_USERNAME` and `PYPI_PASSWORD` secrets


## Workflow

🎯 To trigger the workflow (create a release and upload to PyPI), commit with a 'X.X.X Release' message pattern.
- Pattern: `\d+\.\d+\.\d+ (?i)Release.*`
- Examples ✔️:
    - 1.0.0 Release: First release.
    - 3.2.0 RELEASE
    - 5.0.2 release (foo bar)

**💼 Your jobs:**
1. Finish all your work locally.
2. Update the changelog file (let's say it's for the `3.0.0` release).
3. Pull (`git pull`) any changes from the remote.
4. Make the **last commit** (`git commit -am "3.0.0 Release"`) to trigger the workflow.
5. Push (`git push`) the changes.
6. Wait for the workflow to complete.
7. Pull (`git pull`) again once the workflow updates the `pyproject.toml`.

**🔄 Workflow jobs:**
1. Check the commit message:
    - If it matches the pattern, next.
    - If not, stop the workflow.
2. Inspect the changelog file:
    - If there's more than one changelog file in the docs folder, raise an error.
    - Extract the latest changelog from the file:
        - If it fails to extract, raise an error.
    - Compare the versions (version from the commit message and the latest changelog):
        - If they don't match, raise an error.
3. Update the `pyproject.toml` file:
    - Change the `version = "X.X.X"` component.
    - Make a commit.
4. Create a GitHub release.
5. Publish to PyPI.

> **⭐️Note:** Since the workflow highly depends on the **latest** commit being pushed to the repository, make sure to pull any changes before committing.


## Links

- [Documentation](https://nvfp.github.io/fast-pypi-release)
- [Demo](https://nvfp.github.io/fast-pypi-release/demo)
- [Changelog](https://nvfp.github.io/fast-pypi-release/changelog)
- [Sponsors](https://nvfp.github.io/fast-pypi-release/sponsors)
- [FAQs](https://nvfp.github.io/fast-pypi-release/faqs)


## Troubleshoot

- To report bugs or ask questions, please open an issue or submit a pull request.


## License

This project is licensed under the MIT license.
