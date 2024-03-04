num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

def calculator(num1, num2, operator) :
  if operator == "+":
    result = num1 + num2

  elif operator == "-":
    result = num1 - num2

  elif operator == "*":
    result = num1 * num2

  elif operator == "/":
    result = num1 / num2
  
  else: 
    result = ''
  
  return result

result = calculator(num1, num2, operator)
print(result)
