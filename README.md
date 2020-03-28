# packaged-cli-demo
Dummy CLI using Click, packaged using PyInstaller

## Install for development

```
pip install -e .
```

## PyInstaller single-file build

```
rm -rf build
rm -rf dist
pyinstaller demo/cli.py --name demo-cli --onefile --add-data=demo/version:demo/version --hidden-import="pkg_resources.py2_warn"
```
