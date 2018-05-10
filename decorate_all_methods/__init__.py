"""Iterate through all methods in a class and apply decorator."""


def decorate_all_methods(decorator, exclude=None):
    if exclude is None:
        exclude = []

    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)) and attr not in exclude:
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
