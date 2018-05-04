from bs4 import BeautifulSoup as bs
import requests
import solution


with open('number.txt','r') as f:
    global n
    n = int(f.readline())
with open('number.txt','w') as f:
    f.write(str(n+1))
    
with open('easy-list.txt','r') as f:    
    for i in range(n):
        f.readline()
    global a
    a = f.readline()

source = requests.get('https://www.codechef.com' + a).text
soup = bs(source, 'lxml')
with open('today.txt','w+') as f:
    temp = soup.find('h1').text
    i = 0
    for x in temp:
        i += 1
        if x == ' ' and temp[i+1] == ' ':
            break
        if x == '<':
            i -= 1
            break
    temp = temp[:i]
    f.write(temp + '\n\n')

unProcessed = soup.findAll('div', {'class': 'content'})[1].text
    
with open('today.txt','a') as f:    
    i = 0
    flag = 0
    for x in unProcessed:
        if flag == 1:
            continue
        if x == '<':
            flag = 1
            continue
        if x == '>':
            flag = 0
            continue
        try:
            f.write(x)
        except:
            f.write(str(x.encode('utf8')))



solution.writeSol(a[9:])
