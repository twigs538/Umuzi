def add(*args: int) -> int:
    result = 0

    for integers in args:
        result = result + integers
    
    return result

def multiply(*args: int) -> int:
    result = 1
    number_of_integers = 0
    
    for integers in args:
        number_of_integers = number_of_integers + 1
        result = result * integers

    if number_of_integers == 0:
        result = 0
    elif number_of_integers == 1:
        result = args[0]
        
    return result

if __name__ == '__main__':
    print(add(8))
    print(multiply(1,-6))