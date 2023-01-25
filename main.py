#! /usr/bin/python

import os
from pathlib import Path
import shutil


os.chdir("/storage/emulated/0")


def is_audio(file):
    p= Path(file)
    if p.suffix == ".mp3" or p.suffix ==".m4a":
        return True

for dirPath, dirName, fileNames in os.walk(os.getcwd()):
    for fileName in fileNames:
        if is_audio(fileName):
            print (f"{dirPath}{fileName}")
            shutil.move(f"{dirPath}/{fileName}", "AllAudio")  
