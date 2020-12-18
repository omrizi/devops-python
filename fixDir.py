import os
import shutil

dirList = os.listdir()
cwd = os.getcwd()

for dir in dirList:
    fixed_dir = dir.replace(" ","_").replace(",","")
    if(fixed_dir != dir):
        shutil.move(cwd+"/"+dir,cwd+"/"+fixed_dir)
