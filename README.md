# Bronco-Mates

# How to use

### Enter virtual environment
Using the command line, first go into the virtual environment (http://pypi.python.org/pypi/virtualenv)

If windows cmd
```cmd
venv\Scripts\activate
```

If bash
```bash
source venv/Scripts/activate
```

### Build the project
Once in the virtual environment, run pybuilder

Install pybuilder first if not installed
```bash
pip install pybuilder
```

Install packages listed in requirements.txt
```bash
pip install -r requirements.txt
```

Next build the environment
```bash
pyb
```


# Run the project
Run the script
```bash
./start
```

The server should now be hosted on your local server with port 5000
