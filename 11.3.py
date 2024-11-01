import pprint


class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        type_obj = type(self.obj).__name__
        attributes = [attr for attr in dir(self.obj) if not callable(getattr(self.obj, attr))]
        method = [met for met in dir(self.obj) if callable(getattr(self.obj, met))]
        module_ = self.obj.__class__.__module__
        res = {"type": type_obj, 'attributes': attributes, "methods": method, "module": module_}
        return res


number_info = Introspection(42).introspection_info()
pprint.pprint(number_info)
number_info = Introspection("HELLO").introspection_info()
pprint.pprint(number_info)
number_info = Introspection(False).introspection_info()
pprint.pprint(number_info)
