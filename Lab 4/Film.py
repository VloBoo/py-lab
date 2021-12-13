class Film:
    name = 'Неизвестное название'
    #словарь info = (Краткое описание, Оценка, Год, Кортеж Жанров)
    #                  subdescription   mark    date   tags
    info = ()
    
    def __init__(self, name, info, description, mark, date, genre):
        self.name = name
        self.description = description
        self.info = {'subdescription' : info, 'mark' : mark,'date' : date,'tags' : genre}

    def print_info(self):
        print(f'\nИнформация об фильме\nИмя: {self.name}\nКраткая информация: {self.info["subdescription"]}\n')
        
    def print_full_info(self):
        print(f'\nПолная информация о фильме\n\nНазвание: {self.name}\nКраткая информация: {self.info["subdescription"]}\nОценка: {self.info["mark"]}\t\tГод: {self.info["date"]}\nЖанры: ',end=' ')
        for g in self.info["tags"]:
            print(g,end=',')
        print(f'\n\nОписание: {self.description}\n')
       
# структура файла 
# name\n
# description\n
# subdescriprion\n
# Оценка\n
# Год\n
# Жанр1\n
# Жанр2\n
# ...  
# Жанрn\n
# 0\n 
     
    def toStr(self):
        s=f'{self.name}\n{self.description}\n{self.info["subdescription"]}\n{self.info["mark"]}\n{self.info["date"]}\n'
        for i in self.info['tags']:
            s = f'{s}{i}\n'
        s = f'{s}0\n'
        return s