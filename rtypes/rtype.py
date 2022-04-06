import inspect

class rtype:
    type = None
    predicate = None

    def __init__(self,type,predicate,value):
        self.type = type
        self.predicate = predicate
        self.value = value

    def __eq__(self, others):
        return self.type == others.type and self.predicate(others.value) and self.predicate(self.value)

    def __ne__(self, others):
        return not (self == others)

    def __gt__(self,others):
        pass

    def __lt__(self,others):
        pass

    def __ge__(self,others):
        pass

    def __le__(self,others):
        pass

    def __add_(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        return self.value + others.value
        
    def __sub__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        return self.value - others.value

    def __mul__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        return self.value * others.value

    def __truediv__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        return self.value / others.value

    def __str__(self):
        return f'type: {self.type}\npredicate: {inspect.getsource(self.predicate)}value: {self.value}'

