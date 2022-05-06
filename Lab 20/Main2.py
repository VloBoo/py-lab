import webbrowser
import requests
from bs4 import BeautifulSoup
print('Парсер предназначен для сайта GitHub. Программа пытаеться найти файл из первого URL в дереве репозитория второго URL (Ссылки без Http://)')
str1 = str(input('Введите первый URL\n'))
str2 = str(input('Введите второй URL\n'))
file = ''
url = ''
n = 0
for s in str1:
    if n >= 5:
        file = file + s
    if s =='/':
        n = n + 1
n=0
for s in str2:
    if n < 5:
        url = url + s
    if s =='/':
        n = n + 1

webbrowser.open(url+file, new=2)
print('Наичнаем парсинг файлов github.com/torvalds/linux')

r = requests.get('https://github.com/torvalds/linux')
soup = BeautifulSoup(r.text,features='html.parser')
f = open('./out.txt','w')
for s in soup.findAll('div',role ='row',class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item'):
    f.write('   \nFile: '+s.find('a',class_='js-navigation-open Link--primary').text)
    f.write(' \nCommit: '+s.find('a',class_="Link--secondary").text)# Данная строка может выдавать ошибку из-за того, что github постоянно меняет этот параметр
    f.write('   \nDate: '+s.find('time-ago',class_='no-wrap').text)
    f.write('\n')
f.close()
print('Результат парсінга сохранён в out.txt')
