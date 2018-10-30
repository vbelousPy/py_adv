from lesson_04.task_1 import Context


class ValidationError(Exception):
    pass


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

    def __setattr__(self, name, value):
        error_count = 0
        try:
            RealContext().__setattr__(name, value)
        except TypeError:
            error_count += 1
        try:
            ComplexContext().__setattr__(name, value)
        except TypeError:
            error_count += 1

        if error_count < 2:
            self.__dict__[name] = value
        else:
            raise ValidationError


real_context = RealContext()
real_context.x1 = 12
real_context.x3 = 1.2
print(real_context)

complex_context = ComplexContext(**{"a1": 5j, "a2": 1j, "a3": 1j})
complex_context.s1 = 7j
print(complex_context)

number_context = NumberContext(**{"d0": 0j})
number_context.d1 = 12
print(number_context)
