import datetime
import json
from enum import Enum
from Position import Position
from Person import Person


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        elif isinstance(o, Enum):
            return o.name
        elif isinstance(o, (Position, Person)):
            return o.get_dict()

        return super().default(o)
