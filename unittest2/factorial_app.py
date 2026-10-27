def calc_fact(n):
    if n < 0:
        return "Error: Negative"
    result = 1
    for i in range(2, int(n) + 1):
        result *= i
    return result


print("---Factorial Calculator App---")
number = int(input("Enter Your Number:"))
factorial = calc_fact(number)
print(f"Factorail of Number {number} is {factorial}")