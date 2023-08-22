import os
from pathlib import Path
import logging

# logging stream
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Text_Summerizer"

list_of_files = [
    ".github/workflows/.gitkeep",  # for CI/CD deployments
    f"src/{project_name}/__init__.py",  # constructor file for import operations
    # Whenever we have the constructor file, the src folder is presented as our local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/commpm.py",
    f"src/{project_name}/login/__init__.py",
    f"src/{project_name}/login/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "mail.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) 
    
    # Create a directory if the folder doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")

    else:
        logging.info(f"{filename} already exiists" )


file_size = os.path.getsize('/opt/homebrew/lib/python3.11/site-packages/langchain/document_loaders')
print("File Size is :", file_size)