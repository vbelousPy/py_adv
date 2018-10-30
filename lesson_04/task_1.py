from re import match


class Context:
    context_dict = dict()

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if match("[a-zA-Z]+\\w*", k):
                self.__setattr__(k, v)
            else:
                raise NameError

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        some_value = self.__dict__.get(name)
        if some_value is None:
            raise NameError
        else:
            return some_value

    def __str__(self):
        result = str()
        for k, v in self.__dict__.items():
            result += k + "=" + str(v) + ", "
        return self.__class__.__name__ + " (" + result[:-2] + ")"

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__.items())


my_context = Context(**{"z1": 12, "z2": 9, "z3": 0})
my_context.x1 = 1
my_context.t14 = 23
my_context.w = 7
print(my_context)
print("size =", len(my_context))
