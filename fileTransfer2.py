
import shutil
import os
import time

source = "C:/Users/carso/Github_Repos/Python-Projects/folderA/"

destination = "C:/Users/carso/Github_Repos/Python-Projects/folderB/"
files = os.listdir(source)
currentTime = time.time()
for i in files:
    lastModified = os.path.getmtime(source+i)
    if currentTime - 86400 < lastModified:
        shutil.move(source+i, destination)
