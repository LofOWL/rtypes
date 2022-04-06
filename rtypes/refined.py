from rtype import rtype
from typing import *

class refined(rtype):
    type : Any 
    predicate : Any 

    def __init__(self,*args):
        n = len(args)
        if n == 1 and self.evaluate(args[0]):
            self.value = args[0]
        if n == 3: self.type,self.predicate,self.value = n

    def evaluate(self,value): 
        tp_v = type(value) == self.type
        pr_v = self.predicate(value) if self.predicate != None else lambda x: True
        if not tp_v:
            raise Exception(f"{self.tp}: type not match")
        if not pr_v:
            raise Exception(f"{str(self.predicate)}: predicate not match")
        return True
