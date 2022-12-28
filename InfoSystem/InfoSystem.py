
# Точка входа программы
# Здесь будет вызываться головной метод из класса DataManager
# Что-то вроде init_system()

from Menutext import menu_print, menu_query, menu_head, menu_append, menu_delete, menu_salary
import os
import IO_system
from DataManager import DataManager
from TypeOfDepartments import TypeOfDepartments
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
import QueryManager
from QueryManager import ComparisonOperator as cop
data_manager = DataManager()


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def zaglushka():
    print('Здесь могла бы быть ваша реклама')


def correct_input(str):
    while True:
        ans = input(str)
        if ans.isdecimal:
            return int(ans)
        else:
            print('Это не число!')


def menu(list_command: dict, invate: str):
    flag = True
    while flag:
        print(invate)
        command = input('Команда: > ')
        if command in list_command:
            list_command[command]()
        elif command == "0" or not command:
            flag = False
        else:
            print('Такой команды нет!!!')


def sub_menu_print_base():

    def print_per():
        IO_system.print_a_list_with_indexes(data_manager.persons)

    def print_pos():
        IO_system.print_a_list_with_indexes(data_manager.positions)

    def print_emp():
        IO_system.print_a_list_with_indexes(data_manager.employees)

    print_command = {'1': print_per, '2': print_emp,
                     '3': print_pos, '9': clear}
    menu(print_command, menu_print)


def sub_menu_append():
    append_command = {'1': data_manager.add_person, '2': data_manager.add_employee,
                      '3': data_manager.change_department, '4': data_manager.change_salary, '9': clear}
    menu(append_command, menu_append)


def sub_menu_delete():
    delete_command = {'1': data_manager.delete_employee,
                      '2': zaglushka, '9': clear}
    menu(delete_command, menu_delete)


def sub_menu_query():
    def query_by_dep():
        print(' Выберите отдел:')
        IO_system.print_a_list_with_indexes(QueryManager.search_employees(data_manager, TypeOfDepartments(
            IO_system.select_from_enum(TypeOfDepartments, ' Введите код отдела: '))))

    def query_by_pos():
        print(' Выберите должность:')
        IO_system.print_a_list_with_indexes(QueryManager.search_employees(data_manager, TypeOfDepartments(
            IO_system.select_from_enum(TypeOfPositions, ' Введите код должности: '))))

    def query_by_lvl():
        print(' Выберите уровень:')
        IO_system.print_a_list_with_indexes(QueryManager.search_employees(data_manager, TypeOfLevels(
            IO_system.select_from_enum(TypeOfLevels, ' Введите код уровня: '))))

    def query_by_sol():
        oper_com = {'1': cop.GREATER, '2': cop.GREATER_OR_EQUAL,
                    '3': cop.EQUAL, '4': cop.LESS, '5': cop.LESS_OR_EQUAL}
        flag_s = True
        while flag_s:
            print(menu_salary)
            comm = input('Команда: > ')
            if comm in oper_com:
                IO_system.print_a_list_with_indexes(QueryManager.employees_salary(
                    data_manager, correct_input(' Введите сумму: '), oper_com[comm]))
                # click.pause()
            elif comm == '6':
                IO_system.print_a_list_with_indexes(QueryManager.employees_salary(
                    data_manager, correct_input(' Введите первую сумму: '), oper_com['2'], correct_input(' Введите вторую сумму: '), oper_com['5']))
                # click.pause()
            elif comm == "0" or not comm:    
                flag_s = False
            else:
                print('Такой команды нет!!!')

    query_command = {'1': query_by_dep, '2': query_by_pos,
                     '3': query_by_lvl, '4': query_by_sol, '9': clear}
    menu(query_command, menu_query)


def main():

    try:
        is_ok = True
        IO_system.read_db_json(data_manager)

        # is_ok = IO_system.recover_data_base('statement', data_manager, '.txt')

        if not is_ok:

            print('  Ошибка восстановления базы данных из файла')

            data_manager.init_system()

    except:
        data_manager.init_system()

    head_command = {'1': sub_menu_print_base, '2': sub_menu_append,
                    '3': sub_menu_delete, '4': sub_menu_query, '9': clear}
    menu(head_command, menu_head)
    # IO_system.save_data_base('statement', data_manager, '.txt')
    IO_system.write_db_json(data_manager)


if __name__ == '__main__':
    main()
