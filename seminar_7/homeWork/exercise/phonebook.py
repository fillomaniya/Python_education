def readfile(filename):
    return open(filename).read().split('\n')
 
def scan(data):
    for i in  data:
        print(i)
        
def search(data):
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')

def ending(data):
    print("Bye!")
    exit()

def create(data):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}> Телефонный справочник {}</p>\n'\
        .format(style, data)
    html += '   </body>\n</html>'

    with open('python/seminar_7/homeWork/exercise/index.html', 'w') as page:
        page.write(html)

def create2(data):
    xml = '<xml>\n'
    xml += '   <Телефонный справочник {}>\n'\
        .format(data)
    xml += '</xml>'

    with open('python/seminar_7/homeWork/exercise/data.xml', 'w') as page:
        page.write(xml)
    
data = readfile('python/seminar_7/homeWork/exercise/data.txt') 
dict_command = {'1' :  scan, '2' : search, '3' : ending, '4' : create, '5' : create2} 
 
print('''Команды для работы со справочником:
    * Просмотр всех записей справочника:  - 1
    * Поиск по имени - 2
    * Завершить программу - 3
    * Экспорт в html - 4
    * Экспорт в xml - 5 ''')
 
while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')