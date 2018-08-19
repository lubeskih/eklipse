import json


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            if hasattr(obj, 'serialize'):
                return obj.serialize()
            raise
