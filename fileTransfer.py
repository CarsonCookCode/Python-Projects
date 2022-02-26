
import shutil
import os

source = "C:/Users/carso/Github_Repos/Python-Projects/folderA/"

destination = "C:/Users/carso/Github_Repos/Python-Projects/folderB/"
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
