import os

import send2trash

os.chdir('/Users/kienroro2003')
baconFile = open('bacon.txt', 'w')
baconFile.write("Hello world")
baconFile.close()

send2trash.send2trash('bacon.txt')