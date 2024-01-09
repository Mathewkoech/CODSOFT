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
	print("1. add: ")
	print("2. Substraction: ")
	print("3. multiply: ")
	print("4. divide: ")
	
	choice = input("Enter choice (1/2/3/4)")
	if choice not in ['1', '2', '3', '4']:
		print("Invalid choice")
		return
	num1 = float(input("Enter 1st number: "))
	num2 = float(input("Enter 2nd number: "))
	
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