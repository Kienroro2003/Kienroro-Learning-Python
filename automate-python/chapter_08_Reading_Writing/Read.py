import os


path = os.path.join(os.path.abspath('.'), 'data')
file = open(path, 'r')
print(file.readline())
file.close()