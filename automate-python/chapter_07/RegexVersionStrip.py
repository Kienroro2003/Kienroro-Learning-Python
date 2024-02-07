import re

text = '               kienroro                   '

textRegex = re.compile(r' ')
rs = textRegex.sub('', text)
print(rs)