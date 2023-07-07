""" So we're going to write a program that prints the numbers from 1 to 100 but for multiples of 3 it prints Fizz. So it prints a string of fizz instead of the number and for the multiples of five it prints Buzz for the numbers which are multiples of both 5 and 3 then you're going to print out fizz buzz. And so just to give an idea of what this is going to look like you're going to print out something that is 1, 2, 3, 4, and 5. But instead of where we have a number 3 right here, this instead is going to be the string Fizz and instead of the number 5 this is going to be Buzz.

1
2
Fizz
4
Buzz

"""
def FizzBuzz(max_num):
    numbers = range(1, max_num +1)

    for num in numbers:

        if num % 3 == 0 and num % 5 == 0:
            num = f'{num}: FizzBuzz'
        elif num % 3 == 0:
            num = f'{num}: Fizz'
        elif num % 5 == 0:
            num = f'{num}: Buzz'
        
        print(num)

FizzBuzz(100)