import os

for folderName, subFolders, filenames in os.walk('/Users/kienroro2003/delicious'):
    print('The current folder is ' + folderName)

    for subFolder in subFolders:
        print('SUBFOLDER OF' + folderName + ': ' + subFolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ": " + filename)
    print('')