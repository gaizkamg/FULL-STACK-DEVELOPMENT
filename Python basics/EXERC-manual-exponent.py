def manual_exponent(number1, exponent):
    counter = exponent -1
    total = number1

    while counter > 0:
        total *= number1
        counter -= 1
    return total

""" from functools import reduce
    def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list)) """

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

