import os
import re
from lib.logger import logger
import ast
from lib.parsers import *

def read_file(file,folder=None):
    """
    Reads and returns the content of a file.
    """
    try:
        if folder:
            path=os.path.join(folder,file)
        else:
            path=file
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"Error: {path} not found.")
        return ""

def read_project(folder_name):
    project={}
    # project specific informations are read
    try:
        index=read_file("index.py",folder_name)
        index=index.split("=")[1]
        index=ast.literal_eval(index)
        for k,v in index.items():
            project[k]=read_file(v,folder_name)
        project["folder-name"]=folder_name
        return project
    except Exception as e:
        logger.error(f"Error in read_project: ",e)
        return None
def parse_project(project:dict):
    # In this function project specific parsers applied to the project
    try:
        if project:
            # In here you can apply parsers
            project["recipients"]=parse_recipients(project["recipients"])
            return project
        else:
            return None
    except Exception as e:
        logger.error(f"Error in parse_project: ",e)
        return None