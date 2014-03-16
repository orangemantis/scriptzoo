#Renames files, wrote it to rename images, If I had my Mac, I would have used Automator.

import os
fileLoc = '/USers/Tace/Desktop/family'
newPrefix = 'family_pics_'#set new file prefix here
filesList = os.listdir(path=fileLoc)
manifest = ''
picCount = 1
errorLog = ''

for file in filesList:
    fileName = fileLoc + '/' + file
    ext = file.split('.')
    
    if (len(ext) > 1):
        ext = ext[1]
    else:
        ext = ''
    
    newFileName = fileLoc + '/' + newPrefix + str(picCount) + '.' + ext
    manifest += newFileName + ':: description: ... \r\n'

    try:
        if not (newPrefix in file and 'errorLog' in file):
            os.rename(fileName, newFileName)
            picCount += 1
        else:
            raise Exception(file + ' has already been renamed.')
    except Exception as e:
        if (e):
            errorLog = str(e) + '\r\n'
        else:
            errorLog += 'Error with file: ' + file + '.\r\n'

manifestFile = open(fileLoc + '/' + newPrefix + '.txt' ,'w')
manifestFile.write(manifest)
manifestFile.close()

if (errorLog):
    errorFile = open(fileLoc + '/' + 'errorlog.txt', 'w')
    errorFile.write(errorLog)
    errorFile.close()