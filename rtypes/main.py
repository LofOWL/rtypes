from typing import *
from refined import refined

if __name__ == "__main__":
    # set up refined type
    class not_zero(refined):
        type = int
        predicate = lambda self,x: x != 0

    class zero(refined):
        type = int
        predicate = lambda self,x: x == 0
    
    # set value
    a = not_zero(3)
    b = not_zero(4)
    c = zero(0)

    # check types
    print(f'a {type(a)} {type(not_zero)}')
    print(type(a) == not_zero)

    print(f'c {type(c)} {type(zero)}')
    print(type(c) == zero)

    # functions
    def divide(dividend: not_zero,divisor: not_zero) -> float:
        return dividend / divisor
    
    result = divide(a,c)
    print(result)
