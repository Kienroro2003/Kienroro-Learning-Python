import os
import shutil

# shutil.copy('/Users/kienroro2003/spam.txt', '/Users/kienroro2003/delicious/egg2.txt')
os.chdir('/Users/kienroro2003/')
print(os.getcwd())
shutil.copytree('/Users/kienroro2003/delicious', '/Users/kienroro2003')