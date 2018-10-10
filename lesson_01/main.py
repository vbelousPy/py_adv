from lesson_01.stack_exceptions import *


class Stack:

    def __init__(self, data_type=object(), limit=None):
        self.data_type = type(data_type)
        self.limit = limit if limit is not None else -1
        self.my_stack = list()

    def _push(self, new_element):
        if len(self.my_stack) == 0 and self.data_type == type(object()):
            self.data_type = type(new_element)

        if not self.data_type == type(new_element) and not self.data_type == type(object()):
            raise TypeError
        if not self.limit == -1 and len(self.my_stack) >= self.limit:
            raise LimitExceedError

    def push(self, new_element):
        self._push(new_element)
        self.my_stack.append(new_element)

    def pull(self):
        if len(self.my_stack) > 0:
            result = self.my_stack[-1]
            self.my_stack.remove(result)
            return result
        else:
            raise EmptyStackError

    def count(self):
        return len(self.my_stack)

    def clear(self):
        self.my_stack.clear()

    @property
    def type(self):
        return self.data_type.__name__

    def __str__(self):
        return "\"{}<{}>\"".format(str(type(self).__name__), str(self.type))


def test_stack():
    stack_type = int()
    my_stack = Stack(stack_type)

    try:
        my_stack.push("30")
    except TypeError:
        print(True)

    my_stack.push(30)
    my_stack.push(12)
    print(my_stack.count() == 2)

    print(my_stack.pull() == 12)

    my_stack.clear()
    print(my_stack.count() == 0)

    print(my_stack.type == type(stack_type).__name__)

    my_stack = Stack()
    my_stack.push("test")
    print(my_stack.type == type("test").__name__)


test_stack()
