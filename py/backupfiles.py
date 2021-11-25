import os, shutil
source = input("Enter souce folder name ")
destination = input("Enter destination folder name ")
#source = source + "/" 
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source + file), destination)

