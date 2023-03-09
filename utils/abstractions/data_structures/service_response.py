
import json

class ServiceResponse(list):
    def append(self, value: dict):
        if not isinstance(value, dict):
            raise TypeError()
        super().append(value) 

    def as_json(self):
        return json.dumps(self)

