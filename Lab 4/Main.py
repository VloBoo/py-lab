from Film import Film
films = []
films.append(Film('Мстители','Фильм о супергероях','Локи, сводный брат Тора, возвращается, и в этот раз он не один. Земля оказывается на грани порабощения, и только лучшие из лучших могут спасти человечество. Глава международной организации Щ.И.Т. Ник Фьюри собирает выдающихся поборников справедливости и добра, чтобы отразить атаку. Под предводительством Капитана Америки Железный Человек, Тор, Невероятный Халк, Соколиный Глаз и Чёрная Вдова вступают в войну с захватчиком.','7.9','2012',['Фантастика','Боевик']))
films.append(Film('Шрек','Фильм о крутом огре-мизантропа','Жил да был в сказочном государстве большой зеленый великан по имени Шрэк. Жил он в гордом одиночестве в лесу, на болоте, которое считал своим. Но однажды злобный коротышка — лорд Фаркуад, правитель волшебного королевства, безжалостно согнал на Шрэково болото всех сказочных обитателей. И беспечной жизни зеленого великана пришел конец. Но лорд Фаркуад пообещал вернуть Шрэку болото, если великан добудет ему прекрасную принцессу Фиону, которая томится в неприступной башне, охраняемой огнедышащим драконом.','8','2001',['Мультфильм']))
films.append(Film('Большой куш','Художественный фильм...','Фрэнки Четыре Пальца должен был переправить краденый алмаз из Англии в США своему боссу Эви, но, сделав ставку на подпольный боксерский поединок, он попал в круговорот весьма нежелательных событий. Вокруг него и его груза разворачивается сложная интрига с участием множества колоритных персонажей лондонского дна — русского гангстера, троих незадачливых грабителей, хитрого боксера и угрюмого громилы грозного мафиози. Каждый норовит в одиночку сорвать большой куш.','8.5','2000',['Криминал','Комедия']))
films.append(Film('Бегущий по лезвию','Детектив Декард преследует сбежавших андроидов. Культовый киберпанк Ридли Скотта о человеке и человечности','Отставной детектив Рик Декард вновь восстановлен в полиции Лос-Анджелеса для поиска возглавляемой Роем Батти группы киборгов, совершившей побег из космической колонии на Землю. В полиции считают, что киборги пытаются встретиться с Эндолом Тайреллом, руководителем корпорации, ставящей эксперименты над кибернетическим интеллектом. Рик Декард получает задание выяснить мотивы действий киборгов, а затем уничтожить их','7.7','1982',['Фантастика','Триллер']))
films.append(Film('Назад в будущее','Безумный ученый и 17-летний оболтус тестируют машину времени и наводят шороху в 1950-х','Подросток Марти с помощью машины времени, сооружённой его другом-профессором доком Брауном, попадает из 80-х в далекие 50-е. Там он встречается со своими будущими родителями, ещё подростками, и другом-профессором, совсем молодым.','8.6','1985',['Фантастика','Комедия']))

def do_menu():
    for f in films:
        clear()
        f.print_info()
        print('<1> Информация об фильме\t <2> Завершение программы\t <любая другая цифра> Следующий фильм')
        s = int(input('Выберите действие >'))
        if s == 1:
            clear()
            f.print_full_info()
            input('Нажмите Enter для продолжения...')
        elif s == 2:
            print('Мы будем рады вас видеть снова')
    else:
        clear()
        print('==========================================================================')
        print('Спасибо, что просмотрели все наши фильмы. В будущем фильмы будут дополнены')
        print('==========================================================================')
        
def clear():
    for i in range(1,30):#Очистка экрана
            print()
            
print('Добро пожаловать в меню фильмов')
do_menu()


