import inspect
import typing

def checkargs(function):
    def _f(*arguments):
        for index, argument in enumerate(inspect.getfullargspec(function)[0]):
            argument_type =  arguments[index]
            limit_type = function.__annotations__[argument]
            print(f'{type(argument_type)} {type(limit_type)}')
            limit_type = type(limit_type) if type(limit_type) != type else limit_type
            if type(argument_type) != limit_type:
                raise TypeError(f"{type(argument_type)} {limit_type} : not match")
        return function(*arguments)
    return _f