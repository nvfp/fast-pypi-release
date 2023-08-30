> ⚠️Deprecation notice: This repo has been sunset since August 30, 2023. Visit the next generation [at here](https://github.com/scapeville/action-PyCICD).

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

There are 3 types of workflows:
- Release `Latest`: [https://nvfp.github.io/fast-pypi-release/trigger-latest-release](https://nvfp.github.io/fast-pypi-release/trigger-latest-release)
- Release `Prerelease`: [https://nvfp.github.io/fast-pypi-release/trigger-prerelease-release](https://nvfp.github.io/fast-pypi-release/trigger-prerelease-release)
- Release `Testing`: [https://nvfp.github.io/fast-pypi-release/trigger-testing-release](https://nvfp.github.io/fast-pypi-release/trigger-testing-release)


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
