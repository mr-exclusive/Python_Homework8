from Person import Person
from Position import Position
from TypeOfDepartments import TypeOfDepartments
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
import DataManager

class Employee:
    """Класс СОТРУДНИК

    Имеет атрибуты:
    - department  ->  тип отдела
    - person -> человек
    - position -> должность
    """

    # Устанавливаем определенную типизацию для атрибутов класса
    department: TypeOfDepartments

    person: Person

    position: Position

    def __init__(self, department:TypeOfDepartments, person:Person, position:Position):
        """Метод инициализации для атрибутов класса. 
        
        Поступают значения:
        - depatment
        - person
        - position
        """

        self.department = department

        self.person = person

        self.position = position
                

    def to_string(self):
        """Метод конвертации атрибутов класса в строчный тип
        
        Возвращает форматированную строку текста. """
        return self.person.to_string() + '   ' + \
               self.position.to_string() + ' (' + \
               str(self.department.value) + ')'  
    

    def to_txt_file(self, data_manager:DataManager):
        """Метод создания строки из значений:
        - название отдела
        - индекс человека
        - индекс должности
        
        Возвращает форматированную строку из данных значений"""
        return self.department.name + ' ' + \
               str(data_manager.persons.index(self.person)) + ' ' + \
               str(data_manager.positions.index(self.position))

    def from_txt_file(self, line:str, data_manager:DataManager):
        
        splitted = line.strip().split(' ')

        if len(splitted) < 3:

            return False

        try:
            self.department = TypeOfDepartments[splitted[0]]
            self.person = data_manager.persons[int(splitted[1])]
            self.position = data_manager.positions[int(splitted[2])]

            return True

        except:

            return False

    def get_dict(self):
        obj_as_dict = vars(self)
        return obj_as_dict
