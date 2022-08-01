

# Add func
def add(n1, n2):
  return n1 + n2

# Subrtract func
def subtract(n1, n2):
  return n1 - n2

# Multiply func
def multiply(n1, n2):
  return n1 * n2

# Divide func
def divide(n1, n2):
  return n1 / n2

functions = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What is the first number? \n"))
num2 = int(input("What is the second number? \n"))
operation = input("Which operation would you like to perform? Type:  + , - , * , or / \n")

for key in functions:
  if key == operation:
    op = functions[key]
    op_result = op(num1, num2)
    print(f"{num1} {operation} {num2} = {op_result}")
