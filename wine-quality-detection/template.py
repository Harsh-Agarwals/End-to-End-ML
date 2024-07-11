import os
import logging
from pathlib import Path

logging.basicConfig(filename="wine_prediction.log", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

folder_name = "wine_prediction"

# __init__.py => consider folder as a local package
list_of_files = [
    f"src/{folder_name}/__init__.py", 
    f"src/{folder_name}/components/__init__.py",
    f"src/{folder_name}/utils/__init__.py",
    f"src/{folder_name}/utils/common.py",
    f"src/{folder_name}/config/__init__.py",
    f"src/{folder_name}/config/configuration.py",
    f"src/{folder_name}/pipeline/__init__.py",
    f"src/{folder_name}/entity/__init__.py",
    f"src/{folder_name}/entity/config_entity.py",
    f"src/{folder_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file in list_of_files:
    file = Path(file)
    dirname, filename = os.path.split(file)
    logger.warning(f"\nFile: {file}")
    logger.warning(f"dirname: {dirname}, filename: {filename}")

    if dirname!='':
        if os.path.exists(dirname):
            pass
        else:
            os.makedirs(dirname)
        logger.info(f"=====Making directory {dirname}=====")

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(file, 'w') as f:
            pass
            logger.info(f"=====Created file {filename}=====")
    else:
        logger.error(f"{filename} already exists!")

