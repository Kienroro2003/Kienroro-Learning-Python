import requests

from bs4 import BeautifulSoup as bs



# load the projectpro webpage content

r = requests.get('https://www.projectpro.io/')



# convert to beautiful soup

soup = bs(r.content)



# printing our web page

print(soup.prettify())



# paragraph inside the "div"

content = soup.select('div p')
print(content)