
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels

class Position:
    
    # Зарплата
    salary: float

    # Тип ддолжности
    position_type: TypeOfPositions

    # Уровень должности
    position_level: TypeOfLevels

    def __init__ (self, salary:float,position_type:TypeOfPositions, position_level:TypeOfLevels):

        self.salary = salary

        self.position_type = position_type

        self.position_level = position_level

    # Функция представления должности в виде строки (вывод на консоль)
    def to_string(self):

        return str(self.position_level) + ' ' + str(self.position_type) + ' (' + str(self.salary) + ' рублей)'

    

    # Функция для сохранения всех полей в текстовый файл
    def to_txt_file(self):

        return self.position_type.name + ' ' + \
               self.position_level.name + ' ' + \
               str(self.salary).replace(',','.')

    

    # Функция чтения всех полей их текстовой строки
    def from_txt_file(self, line:str):

        splitted = line.strip().split(' ')

        if len(splitted) < 3:

            return False

        try:
            self.position_type = TypeOfPositions[splitted[0]]
            self.position_level = TypeOfLevels[splitted[1]]
            self.salary = float(splitted[2].replace(',','.'))

            return True

        except:

            return False

    def get_dict(self):
        obj_as_dict = vars(self)
        return obj_as_dict
