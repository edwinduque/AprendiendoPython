
def is_prime(number):
    print(number)
    result = True
    for i in range(2, number):
        if number % i == 0:
            result = False
            break      
    return result

if __name__ == "__main__":
    print("***************************")
    print("**Verifica si un numero es primo o no")
    number = int(input("Digite el numero: "))
    result = is_prime(number)
    
    if result:
        print("es un numero primo")
    else:
        print("no un numero primo")