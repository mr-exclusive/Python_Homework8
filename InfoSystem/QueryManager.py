# Класс, в котором будут все запросы в базу данных и логика из обработки
# Вроде "Найти всех мидл-инженеров с такой-то зарплатой"

import DataManager
from TypeOfDepartments import TypeOfDepartments
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from enum import Enum
import operator
import IO_system


class ComparisonOperator(Enum):
    EMPTY = -1
    GREATER = 1
    GREATER_OR_EQUAL = 2
    LESS = 3
    LESS_OR_EQUAL = 4
    EQUAL = 5


def get_operator(op):
    if op == ComparisonOperator.GREATER:
        return operator.gt
    if op == ComparisonOperator.GREATER_OR_EQUAL:
        return operator.ge
    if op == ComparisonOperator.LESS:
        return operator.lt
    if op == ComparisonOperator.LESS_OR_EQUAL:
        return operator.le
    if op == ComparisonOperator.EQUAL:
        return operator.eq


def compare_salary(salary, salary_from, left_operand, salary_to=-1, right_operand=ComparisonOperator.EMPTY):
    if left_operand != ComparisonOperator.EMPTY:
        left_result = get_operator(left_operand)(salary, salary_from)

        if right_operand != ComparisonOperator.EMPTY:
            return left_result and get_operator(right_operand)(salary, salary_to)
        else:
            return left_result

    return False


# ищем сотрудников по диапазону зарплат
# можно использовать строгое или не строгое неравенство
# а так же сравнивать только с одним значением, тогда второе значение и оператор не передаются
def employees_salary(data_manager: DataManager, salary_from, left_operand, salary_to=-1, right_operand=ComparisonOperator.EMPTY):
    return [empl for empl in data_manager.employees if compare_salary(empl.position.salary,
                                                                      salary_from,
                                                                      left_operand,
                                                                      salary_to,
                                                                      right_operand)]


# ищем сотрудников по отделу
# ищем сотрудников по занимаемой должности
# ищем сотрудников по уровню
def search_employees(data_manager: DataManager, enum_criteria):
    return [empl for empl in data_manager.employees if test_employee(empl, enum_criteria)]


def test_employee(employee, enum_criteria):
    if isinstance(enum_criteria, TypeOfDepartments):
        return employee.department == enum_criteria
    elif isinstance(enum_criteria, TypeOfPositions):
        return employee.position_type == enum_criteria
    elif isinstance(enum_criteria, TypeOfLevels):
        return employee.position_level == enum_criteria
    else:
        return False


# # ищем сотрудников по отделу
# def employees_from_department(data_manager: DataManager, department: TypeOfDepartments):
#     return [empl for empl in data_manager.employees if empl.department == department]
#
# # ищем сотрудников по занимаемой должности
# def employees_of_position(data_manager: DataManager, position: TypeOfPositions):
#     return [empl for empl in data_manager.employees if empl.position.position_type == position]
#
#
# # ищем сотрудников по уровню
# def employees_of_level(data_manager: DataManager, level: TypeOfLevels):
#     return [empl for empl in data_manager.employees if empl.position.position_level == level]
