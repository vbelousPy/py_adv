from lesson_01.stack_exceptions import *


class Stack:

    def __init__(self, data_type=object, limit=None):
        """"Конструктор принимает опциональный аргумент data_type, по умолчанию - object,
        опциональный аргумент limit (int), который определяет максимальный размер стэка, по умолчанию - None."""
        self.data_type = data_type
        self.limit = limit
        self.my_stack = list()

    def _push(self, new_element):
        """"проверяет возможность добавления элемента в стэк (по лимиту и типу).
           В случае несоответствия типов должен генерить исключение TypeError.
           В случае достижения лимита - генерить LimitExceedError."""
        if not self.data_type == type(new_element):
            raise TypeError

        if self.limit is not None and len(self.my_stack) >= self.limit:
            raise LimitExceedError

    def push(self, new_element):
        """добавляет новый объект в стэк"""
        self._push(new_element)
        self.my_stack.append(new_element)

    def pull(self):
        """"извлекает верхний элемент стэка и возвращает его.
        В случае пустого стэка генерит исключение EmptyStackError"""
        if len(self.my_stack) > 0:
            result = self.my_stack[-1]
            self.my_stack.remove(result)
            return result
        else:
            raise EmptyStackError

    def count(self):
        """возвращает количество элементов в стэке"""
        return len(self.my_stack)

    def clear(self):
        """очищает стэк"""
        self.my_stack.clear()

    @property
    def type(self):
        """возвращает тип данных стэка."""
        return self.data_type

    def __str__(self):
        """Возвращающет строку вида Stack<тип данных>"""
        return "\"{}<{}>\"".format(str(type(self).__name__), str(self.type))


def test_stack():
    stack_type = int
    my_stack = Stack(stack_type)

    try:
        my_stack.push("30")
    except TypeError:
        print(True)
    else:
        print(False)

    my_stack.push(30)
    my_stack.push(12)
    print(my_stack.count() == 2)

    print(my_stack.pull() == 12)

    my_stack.clear()
    print(my_stack.count() == 0)

    print(my_stack.type == stack_type)

    my_stack = Stack()
    try:
        my_stack.push("test")
    except TypeError:
        print(True)
    else:
        print(False)
    print(my_stack.type == object)

    my_stack = Stack(limit=0, data_type=int)
    try:
        my_stack.push(1)
    except LimitExceedError:
        print(True)
    else:
        print(False)

    try:
        my_stack.pull()
    except EmptyStackError:
        print(True)
    else:
        print(False)


test_stack()
