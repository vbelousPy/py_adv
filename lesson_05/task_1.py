from re import match


def dict_builder():
    result_dict = dict()
    while True:
        entered_str = input("Enter class argument as (name=value): ")
        if len(entered_str) == 0:
            return result_dict
        temp_list = entered_str.split("=")
        try:
            key = temp_list[0].strip()
            val = temp_list[1].strip()
            if match("^[a-zA-Z]+\\w*$", key) and match("^(\".*\")|(\\d+)|(True)|(False)$", val):
                result_dict.update({key: val})
            else:
                raise ValueError
        except (IndexError, ValueError):
            print("Invalid form string")


def new_str(self):
    result_str = "Class <{}>:".format(str(self.__class__.__name__))
    some_list = [k + " = " + v for k, v in self.__class__.__dict__.items() if
                 not callable(getattr(self, k)) and not k.startswith('__')]
    for i in some_list:
        result_str += "\n" + i
    return result_str


name_class = input("Enter class name: ")
if len(name_class) == 0 or not match("^[a-zA-Z]+\\w*$", name_class):
    raise KeyError

args_class = dict_builder()
args_class.update({"__str__": new_str})

MyClass = type(name_class, (), args_class)
a = MyClass()
print(a)
