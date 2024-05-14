#CODSOFT_TASK_2 - Calculator 


#FUNCTIONS TO PERFORM ARITHMETIC OPERATIONS
def addition(x, y):
    return x + y 

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y                

print("\n\t\t\tWELCOME TO THE CALCULATOR !!")

while True:
    print("\n\tSelect the operations:")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")

    print("4. Division ")
    print("5. Exit")

    choice = input("Enter operation choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
    elif choice == '5':
        print("Bye!")
        break
    else:
        print("Invalid input! Please enter a valid  choice.")
  
                                 #OUTPUT1
                                

'''                     WELCOME TO THE CALCULATOR !! 

Select the operations:
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division 
5. Exit
Enter operation choice (1/2/3/4/5): 1
Enter first number: 23
Enter second number: 44
Result: 67.0

        Select the operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter operation choice (1/2/3/4/5): 2
Enter first number: 45
Enter second number: 76
Result: -31.0

        Select the operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter operation choice (1/2/3/4/5): 3
Enter first number: 22
Enter second number: 5
Result: 110.0

        Select the operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter operation choice (1/2/3/4/5): 4
Enter first number: 23
Enter second number: 0
Result: Error! Division by zero is not allowed.

        Select the operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter operation choice (1/2/3/4/5): 4
Enter first number: 40
Enter second number: 8
Result: 5.0

        Select the operations:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter operation choice (1/2/3/4/5): 5
Bye! 
'''
