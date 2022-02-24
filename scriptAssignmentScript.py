import os
import time

# Find files of type ".txt" and print file name and date last modified.

fPath = "C:\\Users\\carso\\Github_Repos\\Python-Projects\\scriptAssignment"

dirList = os.listdir(fPath)


for i in dirList:
    if ".txt" in i:
        print("{} was last modified on: {}".format(i, time.ctime(os.path.getmtime(os.path.join(fPath, i)))))
