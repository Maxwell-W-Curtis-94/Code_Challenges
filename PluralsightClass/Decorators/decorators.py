import functools


@functools.wraps  # copes meta data
def check_non_negative(index):  # ~wrapper that allows arguments
    def validate(f):  # decorator - takes a callable returns a callable
        def wrap(*args):  # local function
            if args[index] < 0:
                raise ValueError(
                    "Argument {} must be non-negative".format(index)
                )
            return f(*args)

        return wrap

    return validate


@functools.wraps
def second_decorator(f):
    def something():
        pass

    return something


@second_decorator
@check_non_negative(1)  # first decorator called
def simple():
    pass
