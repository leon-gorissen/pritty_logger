To create a new version

1. Update the version number in setup.py
2. Clean your builds

```bash
rm -rf dist/ build/ *.egg-info
```

3. Build wheel and tarball

```bash
python3 -m build
```

4. Publish to pypi

```bash
python3 -m twine upload dist/*
```
