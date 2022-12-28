
# Класс персоны (человека)
from datetime import date
from TypeOfGenders import TypeOfGenders

class Person:

    # Имя
    first_name: str
       
    # Фамилия
    last_name: str
       
    # Отчество
    middle_name: str
        
    # Дата рождения в структуре datetime
    date_of_birth: date

    # Пол
    gender: TypeOfGenders

    # Это "контсруктор" экземпляра класса. 
    # Здесь происходи создание нового человека из внешнего кода
    # self - это ключевое слово, указывающее на то, что это не просто функция,
    # а функция только для экземпляра класса
    def __init__(self, first_name: str, last_name: str, middle_name: str, date_of_birth: date, gender: TypeOfGenders):

        self.first_name = first_name

        self.last_name = last_name

        self.middle_name = middle_name

        self.date_of_birth = date_of_birth

        self.gender = gender


    # Функция представления персоны в виде строки (вывод на консоль)
    def to_string(self):

        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name + ' (' + \
            str(self.date_of_birth.day).zfill(2) + '.' + \
            str(self.date_of_birth.month).zfill(2) + '.' + \
            str(self.date_of_birth.year).zfill(4) + ')'


    # Функция для сохранения всех полей в текстовый файл
    def to_txt_file(self):

        return self.last_name + ' ' + \
               self.first_name + ' ' + \
               self.middle_name + ' ' + \
               str(self.date_of_birth.day).zfill(2) + ' ' + \
               str(self.date_of_birth.month).zfill(2) + ' ' + \
               str(self.date_of_birth.year).zfill(4) + ' ' + \
               str(self.gender.name)

    

    # Функция чтения всех полей их текстовой строки
    def from_txt_file(self, line:str):

        splitted = line.strip().split(' ')

        if len(splitted) < 7:

            return False

        try:
            self.last_name = splitted[0]
            self.first_name = splitted[1]
            self.middle_name = splitted[2]
            self.date_of_birth = date(int(splitted[5]),int(splitted[4]),int(splitted[3]))
            self.gender = TypeOfGenders[splitted[6]]

            return True

        except:

            return False

    def get_dict(self):
        obj_as_dict = vars(self)
        return obj_as_dict
