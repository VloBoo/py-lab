class Film:
    name = 'Неизвестное название'
    #кортеж info = (Краткое описание, Оценка, Год, Кортеж Жанров)
    info = ()
    
    def __init__(self, name, info, description, mark, date, genre):
        self.name = name
        self.description = description
        self.info = (info, mark, date, genre)

    def print_info(self):
        print(f'\nИнформация об фильме\nИмя: {self.name}\nКраткая информация: {self.info[0]}\n')
        
    def print_full_info(self):
        print(f'\nПолная информация о фильме\n\nНазвание: {self.name}\nКраткая информация: {self.info[0]}\nОценка: {self.info[1]}\t\tГод: {self.info[2]}\nЖанры: ',end=' ')
        for g in self.info[3]:
            print(g,end=',')
        print(f'\n\nОписание: {self.description}\n')