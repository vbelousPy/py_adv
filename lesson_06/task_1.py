from lesson_04.task_1 import Context as BaseContext


class Context(object):

    def __init__(self, **kwargs) -> None:
        self.context = BaseContext(**kwargs)

    def __enter__(self):
        for i in self.context:
            globals().update({i[0]: i[1]})
        return self.context

    def __exit__(self, exc_type, exc_val, exc_tb):
        for i in self.context:
            del globals()[i[0]]


with Context(x=1, y=2) as cm:
    # noinspection PyUnresolvedReferences
    print(x, y)

try:
    # noinspection PyUnresolvedReferences
    print(x, y)
except NameError:
    print("Variables not found")
