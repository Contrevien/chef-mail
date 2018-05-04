from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import requests

htmlCodes = {
    '&lt;':'<',
    '&gt;':'>',
    '&sol;':'/',
    '&quot;':'"',
    '&apos;':'\'',
    '&amp;':'&',
    '&laquo;':'<<',
    '&raquo;':'>>',
}


def submissions(name):
    source = requests.get('https://www.codechef.com/status/' + name).text
    soup = bs(source, 'lxml')
    table = soup.findAll('tbody')
    found = ''
    for x in table:
        subs = x.findAll('tr')
        for y in subs:
            if y.find('img')['src'] == '/misc/tick-icon.gif': 
                return y.findAll('a')[1]['href']        
        else:
            return -1

def writeSol(name):
    link = submissions(name)
    if link == -1:
        return -1
    req = Request('https://www.codechef.com' + link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    solSoup = bs(webpage, 'lxml')
    ol = solSoup.find_all('ol')
    lines = []
    for x in ol:
        for y in x.find_all('li'):
            lines.extend(y.find_all('div'))

    with open('today.txt','a') as f:
        f.write('\n\n\n\n\n')
        for x in lines:
            for y in x.text:
                f.write(y)
            f.write('\n')

