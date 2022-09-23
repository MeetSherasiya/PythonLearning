def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZeros(number):
    fac = factorial(number)
    print(f"The Factorial is {fac}")
    count = 0
    while(fac%10 == 0):
        count += 1
        fac = fac/10
    return count

if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print(factorialTrailingZeros(num))