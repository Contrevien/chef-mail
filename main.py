from selenium import webdriver
from pyvirtualdisplay import Display
import solution

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
browser = webdriver.Chrome(chrome_options=options)

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

link = a
url = 'https://www.codechef.com' + a
browser.get(url)
main = browser.find_element_by_tag_name('main')
header = main.find_element_by_tag_name('header')
h1 = header.find_element_by_tag_name('h1')
h1 = h1.text

with open('today.txt','w+') as f:
    f.write(h1 + '\n\n')

a = main.find_elements_by_class_name("mathjax-support")
b = ''
for x in a:
    b += x.text
    b += '\n'

b = b[:b.find('Source Limit:',100)]

with open('today.txt','a') as f:
    for x in b:
        try:
            f.write(x)
        except:
            f.write(x.encode('utf-8'))
browser.quit()

solution.writeSol(link[9:])


