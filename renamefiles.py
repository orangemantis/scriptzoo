#Renames files, wrote it to rename images, If I had my Mac, I would have used Automator.

import os
import shutil
fileLoc = ''#set to dir path of files to be renamed
newPrefix = 'some_pic'#set this to new name prefix of files
filesList = os.listdir(path=fileLoc)
manifest = ''

for file in filesList:
    fileName = fileLoc + '/' + file
    manifest += file + ':: description: ... \r\n'
    shutil.copyfile(fileName, fileLoc + '/' + newPrefix + file)
    os.remove(fileName)

manifestFile = open(fileLoc + '/' + 'descriptions.txt' ,'w')
manifestFile.write(manifest)
manifestFile.close()
