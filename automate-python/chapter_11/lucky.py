#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=python')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.prettify())

# Open a browser tab for each result.
linkElems = soup.select('a:has(h3)')
print(len(linkElems))
numOpen = min(50, len(linkElems))
for i in range(numOpen):
    #webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print(linkElems[i].getText())
