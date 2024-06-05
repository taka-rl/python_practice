import os  

"""
This script creates folders with each name written in the "1_createFolderList.txt".
Each folder has leacture and exam folders.
"""

path = input("Write the place where you would like to make folders:") # as an abs path
absPath = path + "\\"
relPathL = "\\lecture"
relPathE = "\\exam"
print(absPath)
print(absPath + relPathL, relPathE)

with open('1_createFolderList.txt', 'r') as f:
    folderList = f.read().split("\n")

for i in folderList:
    if os.path.exists(absPath + i):
        continue        
    else:
        os.mkdir(absPath + i)
        os.mkdir(absPath + i + relPathL)
        os.mkdir(absPath + i + relPathE)
    
print("end process")
