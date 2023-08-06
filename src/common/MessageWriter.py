"""
Write message into file
"""
import logging as log
import pandas as pd
import os
from pathlib import Path


def write_message(file_name, msg):
    """Write event in file"""
    df = pd.DataFrame(msg)
    val = df.to_string()
    # curr = os.getcwd()
    # log.warning("------current is= %s", curr)

    # path = "../../LogFiles/"+file_name
    # mode = 'a' if os.path.exists(file_name) else 'w+'
    # real = os.path.realpath(path)
    # log.warning("------path is= %s, mode: %s, real=%s", path, mode, real)
    with open(file=file_name, encoding="utf-8", mode='w+') as file:
        log.warning("Writing event data into file= %s, data=%s",file_name, val)
        file.write("Jai Mata DI")
