import datetime
import json
from Position import Position
from Person import Person
from TypeOfPositions import TypeOfPositions
from TypeOfLevels import TypeOfLevels
from TypeOfGenders import TypeOfGenders
from TypeOfDepartments import TypeOfDepartments


class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, *args, **kwargs, object_hook=self.object_hook)

    @staticmethod
    def object_hook(obj):
        ret = {}
        for key, value in obj.items():
            if key == 'date_of_birth':
                ret[key] = datetime.datetime.fromisoformat(value)
            elif key == 'person':
                ret[key] = Person(**value)
            elif key == 'position':
                ret[key] = Position(**value)
            elif key == 'position_type':
                ret[key] = TypeOfPositions[value]
            elif key == 'position_level':
                ret[key] = TypeOfLevels[value]
            elif key == 'department':
                ret[key] = TypeOfDepartments[value]
            elif key == 'gender':
                ret[key] = TypeOfGenders[value]
            else:
                ret[key] = value

        return ret
