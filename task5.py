def factorial(num):
    if num<2:
        return 1
    else:
        return num*factorial(num-1)
    
num=int(input("Enter a number: "))
fact=factorial(num)
print(f"factorial of {num} is: {fact}")

