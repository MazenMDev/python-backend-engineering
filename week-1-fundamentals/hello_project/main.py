# main.py ---- My first production style python script

def get_user_input():
    """Get user information from command line."""

    name = input("what's your name? ")
    age = int(input("How old are you? "))
    monthly_salary = float(input("Enter your monthly salary: "))
    return name, age, monthly_salary

def calculate_finances(monthly_salary):
    """Calculate yearly salary and salary after tax."""

    yearly_salary = monthly_salary * 12
    tax_rate = 0.20
    salary_after_tax = yearly_salary * (1 - tax_rate)
    return yearly_salary, salary_after_tax

def display_summary (name, age, monthly_salary, yearly_salary, salary_after_tax):
    """Print formatted user summary"""

    print("\n" + "="*50)
    print(f"Profile Summary for {name}")
    print("="*50)
    print(f"Age: {age} years old")
    print(f"Monthly Salary: ${monthly_salary:,.2f}") 
    print(f"Yearly Salary: ${yearly_salary:,.2f}")
    print(f"After 20% tax: ${salary_after_tax:,.2f}")
    print("="*50)

def main():
    """Main program entry point."""

    print("Welcome to User Profile Generator!")
    name, age, monthly_salary = get_user_input()
    yearly_salary, salary_after_tax = calculate_finances(monthly_salary)
    display_summary(name, age, monthly_salary, yearly_salary, salary_after_tax)

if __name__ == "__main__":
    main()