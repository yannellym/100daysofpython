import math

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


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
  "−" : subtract,
  "✖️" : multiply,
  "➗" : divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number? \n"))
  num2 = float(input("What is the second number? \n"))
  operation = input("Which operation would you like to perform? Type:  + , − , ✖️ , or ➗ \n")
 
  for key in functions:
    if key == operation:
      op = functions[key]
      op_result = op(num1, num2)
      print(f"{num1} {operation} {num2} = {op_result}")
      should_continue = True
  
  while should_continue:
    operation = input("Which operation would you like to perform? Type:  + , - , * , or / \n")
    num2 = float(input("What is the next number? \n"))
    calculation_func = functions[operation]
    answer = calculation_func(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation \n") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()
calculator()
