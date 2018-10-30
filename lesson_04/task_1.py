from re import match


class Context:
    context_dict = dict()

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self.context_dict.update({k: v})

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


my_context = Context(**{"1k": 12, "_3s": 9, "s2s": 0})
my_context.x1 = 1
my_context.t14 = 23
my_context.w = 7
print(my_context)
# print("size =", len(my_context))
for k, v in my_context:
    print(k, "=", v)
