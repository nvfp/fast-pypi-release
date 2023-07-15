# Fast PyPI release

Create GitHub release and publish to PyPI altogether within a single commit push.


## Installation

1. Copy `fast-pypi-release.yml` and put it under your repository's `.github/workflows` folder.
1. In the `fast-pypi-release.yml` file, search for "EDITME" and update the following:
    - Main branch name
    - PyPI distribution repository name: The name used when installing the package with `pip install`. For example, if using `pip install foo`, the name is `foo`.
    - Git name and email
1. Make sure you have just one changelog file in the `docs` folder:
    - The file can be any extension like `.txt` or `.md`
    - The file's name should include the word "changelog" (case insensitive)
    - Visit [this page](https://nvfp.github.io/fast-pypi-release/demo) to see the allowed format of the changelog
    - The `docs` folder is at the root of your repository
1. Set up your `PYPI_USERNAME` and `PYPI_PASSWORD` as secrets in your repository's GitHub Actions (to be used by Twine for publishing to PyPI):
    1. Visit https://github.com/YOUR_USERNAME/REPOSITORY/settings/secrets/actions
    2. Create `PYPI_USERNAME` and `PYPI_PASSWORD` secrets


## Workflow

🎯 To trigger the workflow (create a release and upload to PyPI), commit with the message pattern below.
- Pattern: `\d+\.\d+\.\d+(b\d*)? (?i)Release.*`
- Examples ✔️:
    - 1.0.0 Release: First release.
    - 3.2.0 RELEASE
    - 5.0.2 release (foo bar)
    - 2.0.0b Release: Testing
    - 2.0.0b3 Release (dev)
    - 2.0.0b913 RELEASE: beta version
    - 1.2.3b4 release: unstable

**💼 Your jobs:**
1. Finish all your work locally.
1. Pull (`git pull`) any changes from the remote (if any).
1. Update the changelog file (let's say it's for the `3.0.0` release).
1. Make the **last commit** (`git commit -am "3.0.0 Release"`) to trigger the workflow.
1. Push (`git push`) the changes.
1. Wait for the workflow to complete.
1. Pull (`git pull`) again once the workflow has updated the `pyproject.toml`.

Click [here](https://nvfp.github.io/fast-pypi-release/demo) to read the demo.

> **⭐️Note:** Since the workflow highly depends on the ***latest*** commit being pushed to the repository, make sure to pull any changes before committing.


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
