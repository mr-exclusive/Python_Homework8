
from enum import Enum

# Перечисление отделов компании

class TypeOfDepartments(Enum):

    # Руководство
    head = 1
    # Управление персоналом
    managment = 2
    # Инженеры
    engineering = 3
    # Обслуживание
    stuff = 4

    pass