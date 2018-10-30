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
        self.context_dict.update({name: value})

    def __getattr__(self, name):
        some_value = self.context_dict.get(name)
        if some_value is None:
            raise NameError
        else:
            return some_value

    def __str__(self):
        result = str()
        for k, v in self.context_dict.items():
            result += k + "=" + str(v) + ", "
        return self.__class__.__name__ + " (" + result[:-2] + ")"

    def __len__(self):
        dict_len = 0
        for k in self.context_dict.keys():
            if match("[a-zA-Z]+\\w*", k):
                dict_len += 1
            else:
                raise NameError
        return dict_len

    def __iter__(self):
        return iter(self.context_dict.items())


class RealContext(Context):

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            super().__setattr__(name, value)
        else:
            raise TypeError("Value must be only (int, float)")


class ComplexContext(Context):

    def __setattr__(self, name, value):
        if isinstance(value, complex):
            super().__setattr__(name, value)
        else:
            raise TypeError("Value must be only complex")


class NumberContext(RealContext, ComplexContext):
    pass


my_context = Context()
my_context.x1 = 1
my_context.t14 = 23
my_context.w = 7
print(my_context)

# real_context = RealContext(**{"a1": 12, "a2": "1", "a3": 0})
real_context = RealContext()
real_context.x1 = 12
# real_context.x2 = "s"
real_context.x3 = 1.2
print(real_context)

complex_context = ComplexContext(**{"a1": 5j, "a2": 1j, "a3": 1j})
complex_context.s1 = 7j
print(complex_context)
print(len(complex_context))
print(real_context)
print(my_context)
