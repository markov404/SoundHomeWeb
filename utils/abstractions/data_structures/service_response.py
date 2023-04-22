
import json


class ServiceResponse(list):
    def append(self, value: dict):
        if not isinstance(value, dict):
            raise TypeError()
        super().append(value)

    def as_json(self) -> str:
        return json.dumps(self)

    def as_one_dictionary(self) -> dict:
        output = {}
        for datapoint in self:
            output.update(datapoint)
        return output

    def as_json_v2(self) -> str:
        return json.dumps(self.as_one_dictionary())
