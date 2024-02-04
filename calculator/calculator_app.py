def add(a, b):
	return a + b
def substraction(a, b):
	return a - b
def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		print("Cannnot divide by zero")
	return a / b

def calculator():
	print("Simple calculator")
	print("1. Add: ")
	print("2. Substraction: ")
	print("3. Multiply: ")
	print("4. Divide: ")
	
	choice = input("Enter choice (1/2/3/4)")
	if choice not in ['1', '2', '3', '4']:
		print("Invalid choice")
		return
	
	try:
		num1 = float(input("Enter 1st number: "))
		num2 = float(input("Enter 2nd number: "))
	except ValueError:
		print("Invalid input. Please enter valid numbers.")
		return

	
	if choice == '1':
		result = add(num1, num2)
		
	elif choice == '2':
		result = substraction(num1, num2)
			
	elif choice == '3':
		result = multiply(num1, num2)

	elif choice == '4':
		result = divide(num1, num2)
	
	print("Result: {}".format(result))

if __name__ == "__main__":
	calculator()