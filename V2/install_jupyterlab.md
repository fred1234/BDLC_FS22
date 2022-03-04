# Installing JupyterLab

As `hadoop`:

```bash
pip install jupyterlab
```

```bash
jupyter notebook --generate-config
```

If this command does not work, sign out of your session (type `exit` until you are back on your local machine). Sign in again and the above command should work.

```bash
jupyter notebook password
```

Copy the hashed password starting from `argon` to the end.

```bash
cat /home/hadoop/.jupyter/jupyter_notebook_config.json
```

## Configs

```bash
nano /home/hadoop/.jupyter/jupyter_notebook_config.py
```

Change the password settings from `# c.NotebookApp.password = ''` to your personal password:

```text
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=...YOUR_HASH...'
```

`JupyterLab` can't be accessed remotely by default. Let's change that by
setting the listen ip from `# c.NotebookApp.ip = 'localhost'` to:

```python
c.NotebookApp.ip = '*'
```

and the default port `# c.NotebookApp.port = 8888` to:

```python
c.NotebookApp.port = 8888
```

In addition, we don't want to auto launch a browser. Change `# c.NotebookApp.open_browser = True` to:

```python
c.NotebookApp.open_browser = False
```

start the service with:

```bash
jupyter lab
```

And test the service in your web-browser with the url `http://bdlc-XX.el.eee.intern:8888/lab`

## NodeJS

`nodejs` is missing, as we can see in the logs:

```log
[W 2022-03-03 10:49:14.561 LabApp] Could not determine jupyterlab build status without nodejs
```

Let's install it, as user `student`, with:

```bash
sudo apt install nodejs
```

## Running JupyterLab in the background

Switch back to user `hadoop`.

```bash
nohup jupyter lab > error.log &
```

To stop it, we need to know the `pid`

```bash
ps -ef | grep jupyter
```

e.g output like:

```text
hadoop    152556  152476  6 11:06 pts/0    00:00:01 /usr/bin/python3 /home/hadoop/.local/bin/jupyter-lab
```

Then kill the process with:

```bash
kill 152556
```
