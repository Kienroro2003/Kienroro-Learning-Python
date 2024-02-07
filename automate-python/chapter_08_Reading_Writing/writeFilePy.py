import pprint, os
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

print(os.path.exists(os.path.join(os.path.abspath("."), 'myCats.py')))
if os.path.exists(os.path.join(os.path.abspath("."), 'myCats.py')):
    import myCats
    pprint.pprint(myCats.cats)

