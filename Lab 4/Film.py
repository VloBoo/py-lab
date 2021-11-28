class Film:
    name = 'Неизвестное название'
    #словарь info = (Краткое описание, Оценка, Год, Кортеж Жанров)
    #                  subdescriprion   mark    date   tags
    info = ()
    
    def __init__(self, name, info, description, mark, date, genre):
        self.name = name
        self.description = description
        self.info = {'subdescriprion' : info, 'mark' : mark,'date' : date,'tags' : genre}

    def print_info(self):
        print(f'\nИнформация об фильме\nИмя: {self.name}\nКраткая информация: {self.info["subdescriprion"]}\n')
        
    def print_full_info(self):
        print(f'\nПолная информация о фильме\n\nНазвание: {self.name}\nКраткая информация: {self.info["subdescriprion"]}\nОценка: {self.info["mark"]}\t\tГод: {self.info["date"]}\nЖанры: ',end=' ')
        for g in self.info["tags"]:
            print(g,end=',')
        print(f'\n\nОписание: {self.description}\n')