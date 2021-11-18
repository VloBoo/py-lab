class Film:
    name = 'Неизвестное название'
    info = 'Неизвестная информация'
    mark = '-'
    description = 'Неизвестно'
    date = '----'
    genre = ['Неизвестно','Известно']
    
    def __init__(self, name, info, description, mark, date, genre):
        self.name = name
        self.info = info
        self.mark = mark
        self.date = date
        self.description = description
        self.genre = genre

    def print_info(self):
        print(f'\nИнформация об фильме\nИмя: {self.name}\nКраткая информация: {self.info}\n')
        
    def print_full_info(self):
        print(f'\nПолная информация о фильме\n\nНазвание: {self.name}\nКраткая информация: {self.info}\nОценка: {self.mark}\t\tГод: {self.date}\nЖанры: ',end=' ')
        for g in self.genre:
            print(g,end=',')
        print(f'\n\nОписание: {self.description}\n')