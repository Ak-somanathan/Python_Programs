# pip - A python package installer used to install, upgrade, remove and manage python packages

''' pip install requests
    pip install pytest
    pip install django==5.2
    pip install numpy>=5.0
    pip install django requests pytest '''

# Virtual env - An isolated py env that keeps a project packages separate from other project

# Create a project
''' mkdir myproject
    cd myproject '''

# create a virtual env
''' python -m venv env 
    python -m venv .venv '''

# Activate virtual env
''' .\venv\Scripts\Activate.ps1 
    venv\Scripts\activate '''

# deactivate env
''' deactivate '''

# delete virtual env
''' Remove-Item -Recurse -Force venv '''

# py version
''' python --version '''

# check pip 
''' pip --version 
    python -m pip '''

# upgrade pip
''' python -m pip install --upgrade pip'''

# upgrade package
''' pip install --upgrade django '''

# check installed packages
''' pip list '''

# check outdated packages
''' pip list --outdated '''

# show package information
''' pip show django '''

# freeze dependencies
''' pip freeze '''

# create req.txt
''' pip freeze > requirements.txt '''

# install from req.txt
''' pip install -r requirements.txt '''

# uninstall package
''' pip uninstall requests '''

# .gitignore - never push your virtul env to github
# create .gitignore
''' .gitignore '''
# Add
''' venv/
    .venv/
    __pycache__/
    *.pyc
    .env '''