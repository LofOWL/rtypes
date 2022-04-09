from rtype import rtype
from typing import *

class refined(rtype):
    type : Any 
    predicate : Any 

    def __init__(self,*args):
        n = len(args)
        if n == 1:
            self.value = self.type(args[0])
        if n == 3: 
            self.type = n[0]
            self.predicate = n[1]
            self.value = self.type(n[2])
        if self.predicate == None: self.predicate = lambda x: True

        self.__evaluate__()

    def __evaluate__(self): 
        tp_v = self.type == type(self.value)
        value = self.value.value if issubclass(type(self.value),rtype) else self.value
        pr_v = self.predicate(value)
        if not tp_v:
            raise Exception(f"{type(value)} and {self.type}: type not match")
        if not pr_v:
            raise Exception(f"{self.value} and {type(self)}: predicate not match")
        return True

