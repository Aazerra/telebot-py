from dataclasses import dataclass, is_dataclass
from typing import Union, get_args, get_origin


def nested_dataclass(*args, **kwargs):

    def wrapper(check_class):

        # passing class to investigate
        check_class = dataclass(check_class, **kwargs)
        o_init = check_class.__init__

        def __init__(self, *args, **kwargs):

            for name, value in kwargs.items():

                # getting field type
                ft = check_class.__annotations__.get(name)
                if get_origin(ft) is Union:
                    ft = get_args(ft)[0]

                if is_dataclass(ft) and isinstance(value, dict):
                    obj = ft(**value)
                    kwargs[name] = obj
                o_init(self, *args, **kwargs)
        check_class.__init__ = __init__

        return check_class

    return wrapper(args[0]) if args else wrapper
