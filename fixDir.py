import os
import shutil
import sys

print ("printing argv[1]" +sys.argv[1])
print ("len of argv is :" +str(len(sys.argv)))
print (str(sys.argv))

if(len(sys.argv) > 1):
    cwd = sys.argv[1]
else:
    cwd = os.getcwd()
dirList = os.listdir(cwd)

for dir in dirList:
    fixed_dir = dir.replace(" ","_").replace(",","")
    if(fixed_dir != dir):
        shutil.move(cwd+"/"+dir,cwd+"/"+fixed_dir)
