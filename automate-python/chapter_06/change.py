#! python3

import pyperclip
text = pyperclip.paste()

text = ' '.join(text.split('\r\n'))

pyperclip.copy(text)

'''
You could write code that searches for each \n newline character in the string and then adds the star just after that. But it would be easier to use the split() method to return a list of strings, one for each line in the original string, and then add the star to the front of each string in the list
'''

