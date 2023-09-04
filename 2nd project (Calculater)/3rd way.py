
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num_1, "+", num_2, "=", add(num_1, num_2))

        elif choice == '2':
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))

        elif choice == '3':
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))
            
        elif choice == '4':
            print(num_1, "/", num_2, "=", divide(num_1, num_2))