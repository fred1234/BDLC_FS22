
# JupyterLab Formatting

```bash
pip install jupyterlab_code_formatter
pip install black isort
pip install xmlformatter
```

restarting `JupyterLab`

## Formatting Python Code

In a Notebook (`*.ipynb` files), one can see a new Icon to format the code.

## Formatting XML

Unfortunately, I did not manage to get the `jupyterlab_code_formatter` working in the File Viewer of `JupyterLab`.

However, you can format it in bash with e.g.

```bash
hadoop@bdlc-test:~/hadoop/etc/hadoop$ xmlformat core-site.xml 
```

Another option is to use [Visual Studio Code Remote SSH](https://code.visualstudio.com/docs/remote/ssh-tutorial).

## Resources

- [jupyterlab plugin](https://jupyterlab-code-formatter.readthedocs.io/en/latest/installation.html#installation-step-2-installing-a-supported-code-formatter)
- [xmlformatter](https://pypi.org/project/xmlformatter/)
