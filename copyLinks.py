#File to find all the links in the easy section of CodeChef
from bs4 import BeautifulSoup as bs
import requests

source = requests.get('https://www.codechef.com/problems/easy/').text
soup = bs(source, 'lxml')
probs = soup.findAll('div', {'class':'problemname'})
links = []
for p in probs:
    links.append(p.find('a'))
with open('easy-list.txt', 'w+') as f:
    for l in links:
        f.write(l['href'] + '\n')
