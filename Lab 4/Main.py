from Film import Film
films = []

def menu():
    if len(films) == 0:
        print('В list.film не обнаруженно фильмов')
        print('Предлагаем создать фильм')
        creatFilm()
    for f in films:
        key = 1
        while(key == 1):
            clear(30)
            f.print_info()
            print('<1> Информация об фильме\t<2> Следующий фильм\t<3> Информация о нас\n<4> Завершение программы\t<5> Добавить фильм')
            s = int(input('Выберите действие> '))
            if s == 1:
                clear(30)
                f.print_full_info()
                input('Нажмите Enter для продолжения...')
            elif s == 2:
                key = 0
            elif s == 3:
                clear(30)
                print('Приложение создано: Черняковым Владиславом ("https://github.com/VloBoo/py-lab/tree/master/Lab%204")')
                input('Нажмите Enter для продолжения...')
            elif s == 4:
                return
            elif s == 5:
                clear(30)
                creatFilm()
            elif s == 6:
                print()
            else:
                print('Введенное значение не распознано')
    else:
        print("!!!!!!!!!")
def clear(n):
    if n <= 0:
        return
    print()
    clear(n-1)
    
def initFilms():
        file = open('V:\\Конспекты\\2 Курс\\ИнструментыПО\\Лабы\\Lab 4\\list.film','r')
        name ='1'
        while name !='': 
            name = read_(file)
            if(name ==''):
                break
            description = read_(file)
            subdescription = read_(file)
            mark = float(read_(file))
            date = int(read_(file))
            janl = []
            jan = read_(file)
            while not(jan == '0' or jan ==''):
                janl.append(jan)
                jan = read_(file)
            films.append(Film(name, subdescription, description, mark, date, tuple(janl)))
   
def read_(file):
    s = file.read(1)
    ss=''
    while not(s =='\n' or s ==''):
        
        ss = ss + s
        s = file.read(1)
    return ss    
   
def creatFilm():
    name = input('Введите название фильма:')
    subdescription = input('Введите краткое описание фильма:')
    description = input('Введите полное описание фильма:')
    mark = float(input('Введите оценку фильма:'))
    date = int(input('Введите год фильма:'))
    print('Введите жанры фильма(для остановни ввода введите 0)')
    jan = input()
    janl=[]
    while jan != '0':
        janl.append(jan)
        jan = input()
    f = Film(name, subdescription, description, mark, date, tuple(janl))
    films.append(f)
    file = open('V:\\Конспекты\\2 Курс\\ИнструментыПО\\Лабы\\Lab 4\\list.film','a')
    file.write(f.toStr())
    file.close()
    input('Нажмите Enter для продолжения')    
    

print('Добро пожаловать в меню фильмов')
try:
    initFilms()
    menu()
    clear(30)
    print('''
==========================================================================
Спасибо, что просмотрели все наши фильмы. В будущем фильмы будут дополнены
==========================================================================


                      ############## 
                     ##  ############# 
                     ### ############# 
                     ##################
                      #################
                             ##########
           ############################  ++++++++
         #############################  +++++++++++
         #############################  +++++++++++
        ############################    ++++++++++++
        #############                  +++++++++++++
        ############    ++++++++++++++++++++++++++++
         ###########  +++++++++++++++++++++++++++++
         ###########  +++++++++++++++++++++++++++++
           ########  ++++++++++++++++++++++++++++
                     ++++++++++
                     +++++++++++++++++ 
                     ++++++++++++++++++
                      +++++++++++++  ++
                      +++++++++++++ +++
                        ++++++++++++++
                     
                     
''')
except:
    print('Ошибка выполнения программы, проверьте, существует ли файл list.film')
input('Нажмите Enter для завершения')


