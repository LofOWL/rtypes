from typing import *
from refined import refined

if __name__ == "__main__":
    # set up refined type
    class not_zero(refined):
        type = int
        predicate = lambda self,x: x != 0

    class dividor(refined):
        type = not_zero
        predicate = lambda self,x : x > 0

    class zero(refined):
        type = int
        predicate = lambda self,x: x == 0

    class even(refined):
        type = int
        def predicate(self,number):
            return number % 2 == 0
    
    class odd(refined):
        type = int
        def predicate(self,number):
            return number % 2 != 0

    # set value
    divisor_list : List[dividor] = [dividor(i) for i in range(1,100)]
    test_list : List[str] = [i for i in range(100)]
    c = zero(0)

    A = even(2)
    B = even(4)
    C = odd(5)
    D = odd(7)

    # check types
    print(f'{type(A)} {type(B)} {type(C)}')
    print(type(A) == type(B))
    print(type(A) == type(C))

    # functions
    def divide(dividend: not_zero, divisor: dividor) -> float:
        return dividend / divisor

    def alwaysOdd(num:even,num1:odd) -> odd:
        return num + num1

    def alwaysEven(num:odd,num1:odd) -> even:
        return even(num + num1)

    # results
    print(divide(divisor_list[0],divisor_list[1]))
    print(divide(divisor_list[1],divisor_list[4]))
    print(alwaysOdd(A,C))
    print(alwaysOdd(A,B))
    print(alwaysEven(C,D))
    print(alwaysEven(C,C))