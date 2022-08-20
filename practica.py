#Super listas y diccionarios 

from math import sqrt
from functools import reduce


def main():
    super_list = [
        {"primero": "fabio" },
        {"segundo": "perruno"}
    ]

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    super_dic = {
        "number": [1,2,3,4,5],
        "primari": [ 1,3,5,7,11]
    }

    for key, value in super_dic.items():
        print(f'{key} - {value}')


#List comprehesiond

def lista():
    square = []

    for i in range(1, 10):
        square.append(i**2)

    print(square)

    list_comprehensiond = [i**2 for i in range(1, 20) if i % 3 != 0]

    print(list_comprehensiond)
        
#Dict comprehesion

def diccio():
    my_dict = {}

    for i in range(1,11):
        my_dict[i] = i**3

    print(my_dict)

    dict_comprehension = {i: i**3 for i in range(1, 21)if i % 3 != 0}

    print(dict_comprehension)

    #raiz cuadrada

    #normal modo 

    dictionary = {i: round(i**0.5, 2) for i in range(1, 101) }
    print(dictionary.values())

    #con el modulo sqrt()

    my_dict2 = {i: round(sqrt(i),2) for i in range (1, 11)}
    print(my_dict2)

#Lambda Fucion

def palindrome(string):
    return string == string[::-1]

print(palindrome("ana"))


palindrome = lambda string: string == string[::-1]

try:
    print(palindrome("ana"))
except TypeError:
    print("Solo se puede ingresar Texto")
    

# High order functions

#Filter
def filter():
    My_list = [1, 2, 5, 19, 8, 9, 3]

    odd_number = list(filter(lambda x: x%2 != 0, My_list))

    print(odd_number)

#Map
def map():
    My_list = [1, 2, 3, 4, 5, 6]

    squares = list(map(lambda x: x**2, My_list))

    print(squares)

#reduce
def reduc():
    My_list = [2, 2, 2, 2, 2, 2, 2]

    number = list(reduce(lambda x, a: x*a, My_list))

    print(number)

# Try Except

def divisor(num):
    divisor = [i for i in range(1, num+1) if num % i == 0]

    return divisor


def corne():
    try:
        num = int(input("Ingrese un Número: "))
        print(divisor(num))
        print("Gracias por Utilizar el Programa")
    except ValueError:
        print("Debes Ingresar un Número")


# Assert statements

def palin(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia "    
    return string == string[::-1]

print(palin("ana"))

    
def divisor(num):
    divisors = [i for i in range(1,num+1) if num%i == 0]
        
    return divisors

def runner():
    num = input('Enter a number: ')
    assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
    print(divisor(int(num)))
    print('Finish')


if __name__ == "__main__":
    pass