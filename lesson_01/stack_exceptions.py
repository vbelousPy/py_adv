class LimitExceedError(Exception):

    def __init__(self, *args):
        self.message = args

    def __str__(self):
        return str(self.message)


class EmptyStackError(Exception):

    def __init__(self, *args):
        self.message = args

    def __str__(self):
        return str(self.message)
