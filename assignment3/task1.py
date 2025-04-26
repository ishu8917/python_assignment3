# Task 1: Calculate Factorial Using a Function 

def factorial(n):
    
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))


num = int(input("Enter the number for which you want the factorial: "))
print("The factorial of",num,"is:",factorial(num))