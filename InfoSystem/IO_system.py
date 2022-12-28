# для работы с файлами и вводом/выводом

import os
from enum import Enum
import json
from DataManager import DataManager
from datetime import date
from Person import Person
from Position import Position
from Employee import Employee
from TypeOfGenders import TypeOfGenders
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from TypeOfDepartments import TypeOfDepartments
from CustomJSONEncoder import CustomJSONEncoder
from CustomJSONDecoder import CustomJSONDecoder


def save_data_base(file_name:str, data_manager:DataManager, extention:str):

    if extention.lower() == '.txt':

        with open(file_name + '_persons' + extention, 'w', encoding="utf-8") as file:
            file.write(str(len(data_manager.persons)) + '\n')

            for person in data_manager.persons:
                file.write(person.to_txt_file() + '\n')

        with open(file_name + '_positions' + extention, 'w', encoding="utf-8") as file:
            file.write(str(len(data_manager.positions)) + '\n')

            for position in data_manager.positions:
                file.write(position.to_txt_file() + '\n')

        with open(file_name + '_employees' + extention, 'w', encoding="utf-8") as file:
            file.write(str(len(data_manager.employees)) + '\n')

            for employee in data_manager.employees:
                file.write(employee.to_txt_file(data_manager) + '\n')

    else:

        print('Расширение ' + extention + ' не поддерживается')


def recover_data_base(file_name:str, data_manager:DataManager, extention:str):

    if extention.lower() == '.txt':

        with open(file_name + '_persons' + extention, 'r', encoding="utf-8") as file:
            lines = file.readlines()

            try:

                data_manager.persons = []

                count = int(lines.pop(0).strip())

                for i in range(0, count):

                    new_person = Person('', '', '', date(2000, 1, 1), TypeOfGenders.male)

                    try:

                        new_person.from_txt_file(lines.pop(0))

                        data_manager.persons.append(new_person)

                    except:

                        continue

            except:

                return False



        with open(file_name + '_positions' + extention, 'r', encoding="utf-8") as file:
            lines = file.readlines()

            try:

                data_manager.positions = []

                count = int(lines.pop(0).strip())

                for i in range(0, count):

                    new_position = Position(0.0, TypeOfPositions.boss, TypeOfLevels.junior)

                    try:

                        new_position.from_txt_file(lines.pop(0))

                        data_manager.positions.append(new_position)

                    except:

                        continue

            except:

                return False



        with open(file_name + '_employees' + extention, 'r', encoding="utf-8") as file:
            lines = file.readlines()

            try:

                data_manager.employees = []

                count = int(lines.pop(0).strip())

                for i in range(0, count):

                    new_employee = Employee(TypeOfDepartments.engineering, None, None)

                    try:

                        new_employee.from_txt_file(lines.pop(0), data_manager)

                        data_manager.employees.append(new_employee)

                    except:

                        continue

            except:

                return False

        return True

    else:

        print('Расширение ' + extention + ' не поддерживается')

        return False


def read_statement(file_name:str):
    with open (file_name, 'r', encoding="utf-8") as file:
        result = json.load(file)

    # Функция чтения файла состяния базы
    # вызываем в начале работы программы из DataManager
    # На входе имя файла или полный путь к нему
    # На выходе кортеж типа (persons, position, departments, employees)

    return result


def write_statement(statement, file_name:str):
    with open (file_name,'w', encoding="utf-8") as file:
        json.dump(statement, file)

    # Функция записи состояния базы данных в файл
    # вызываем в конце работы программы из DataManager
    # На входе кортеж типа (persons, position, departments, employees)

    return


def read_db_json(data_manager: DataManager):
    data_manager.persons = get_data('persons', Person)
    data_manager.employees = get_data('employees', Employee)
    data_manager.positions = get_data('positions', Position)


def get_data(table_name, obj_type):
    file_name = table_name + '.json'
    data = []

    if os.path.isfile(file_name):
        if os.stat(file_name).st_size != 0:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = [obj for obj in map(lambda x: obj_type(**x), json.load(f, cls=CustomJSONDecoder))]

    return data


def write_db_json(data_manager: DataManager):
    save_data(data_manager.persons, 'persons')
    save_data(data_manager.employees, 'employees')
    save_data(data_manager.positions, 'positions')


def save_data(data, table_name):
    with open(table_name + '.json', 'w', encoding='utf-8') as f:
        json.dump(list(map(lambda x: x.get_dict(), data)), f, cls=CustomJSONEncoder, ensure_ascii=False)


def read_index(message:str, minIndex:int, maxIndex:int):

    index = minIndex - 1

    while index < minIndex or index > maxIndex:

        index = int(input(message)) - 1

    return index


def print_a_list_with_indexes(list_to_print):

    index = 1

    for item in list_to_print:

        print(str(index) + '. ' + item.to_string())

        index += 1


def select_from_enum(enm:Enum, message:str):

    for dt in enm:

        print(str(dt.value) + ': ' + str(dt.name))

    availableDepartmentCodes = [e.value for e in enm]

    selectedDepartment = -1

    while selectedDepartment not in availableDepartmentCodes:

        selectedDepartment = int(input(message))

    return selectedDepartment
