import os
import logging
import pathlib as Path
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name="TextSummarizer"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filedir in list_of_files:
    path,file=os.path.split(filedir)
    if path!="":
        os.makedirs(path,exist_ok=True)
        print("Making directory",path)
    if (not os.path.exists(filedir)) or (os.path.getsize(filedir)==0):
        with open(filedir,'w') as f:
            pass
            print("Creating Empty file",filedir)
            
    else:
        print("Already Exists")