import inspect

class rtype:
    type = None
    predicate = None

    def __init__(self,type,predicate,value):
        self.type = type
        self.predicate = predicate
        self.value = value

    def __eq__(self, others):
        isSameType = self.type == others.type if issubclass(type(others),rtype) else type(self.value) == type(others)
        value = others.value if issubclass(type(others),rtype) else others
        isSamePredicate = self.predicate(value)
        isSameValue = self.value == value
        return isSameType and isSamePredicate and isSameValue

    def __ne__(self, others):
        return not (self == others)

    def __gt__(self,others):
        return self == others and self.value > others.value

    def __lt__(self,others):
        return self == others and self.value < others.value

    def __ge__(self,others):
        return self == others and self.value >= others.value

    def __le__(self,others):
        return self == others and self.value <= others.value

    def __add__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        value = self.value + others.value
        if self.predicate(value):
            print(f'{self.value} {others.value} {value}')
            return rtype(self.type,self.predicate,value)
        return value
        
    def __sub__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        value = self.vlaue - others.value
        if self.predicate(value):
            return rtype(self.type,self.predicate,value)
        return value

    def __mul__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        value = self.value * others.value
        if self.predicate(value):
            return rtype(self.type,self.predicate,value)
        return value

    def __truediv__(self,others):
        if self.type != others.type:
            raise TypeError(f'unsupported operand type(s) for -: {self.type} and {others.type}')
        value = self.value * others.value
        if self.predicate(value):
            return type(self.type,self.predicate,value)
        return value

    def __str__(self):
        return f'type: {self.type}\npredicate: {inspect.getsource(self.predicate)}value: {self.value}'

