# Workflow jobs

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