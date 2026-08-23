def get_numbers():
  """Get two numbers from user input."""

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  return num1, num2

def calculate(num1, num2):
  """Calculate total, differenece, product and quotient"""
  
  total = num1 + num2
  difference = num1 - num2
  product = num1 * num2
  if num2 == 0:
    quotient = "Cannot divide by zero"
  else:
    quotient = num1 / num2
  return total, difference, product, quotient

def display_summary(total, diff, prod, quot):
  """Print formatted calculation summary"""

  print("="*50)
  print("Your Summary Calculation")
  print("="*50)
  print(f"Sum: {total}")
  print(f"Difference: {diff}")
  print(f"Product: {prod}")
  print(f"Quotient: {quot:.2f}")

def main():
  """Main program entry point."""

  first_number, second_number = get_numbers()
  total, diff, prod, quot = calculate(first_number, second_number)
  display_summary(total, diff, prod, quot)

if __name__ == "__main__":
    main()
