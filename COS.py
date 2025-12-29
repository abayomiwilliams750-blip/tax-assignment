#For the Personal Income Tax Calculator (2009 Tax Brackets)
# This program calculates U.S. federal personal income tax...
# based on filing status and taxable income.

# Prompt the user to enter filing status
print("Filing Status:")
print("0 - Single filer")
print("1 - Married filing jointly / Qualified widow(er)")
print("2 - Married filing separately")
print("3 - Head of household")

status = int(input("Enter your filing status (0-3): "))
income = float(input("Enter your taxable income: "))

tax = 0  # Variable that will store total tax.


# Function to calculate tax based on brackets
def calculate_tax(income, brackets):
    tax_amount = 0
    for rate, lower, upper in brackets:
        if income > lower:
            taxable_part = min(upper, income) - lower
            tax_amount += taxable_part * rate
        else:
            break
    return tax_amount


# Tax brackets for each filing status
if status == 0:  # For Single filer
    brackets = [
        (0.10, 0, 8350),
        (0.15, 8350, 33950),
        (0.25, 33950, 82250),
        (0.28, 82250, 171550),
        (0.33, 171550, 372950),
        (0.35, 372950, income)
    ]

elif status == 1:  # For Married filing jointly
    brackets = [
        (0.10, 0, 16700),
        (0.15, 16700, 67900),
        (0.25, 67900, 137050),
        (0.28, 137050, 208850),
        (0.33, 208850, 372950),
        (0.35, 372950, income)
    ]

elif status == 2:  # For Married filing separately
    brackets = [
        (0.10, 0, 8350),
        (0.15, 8350, 33950),
        (0.25, 33950, 68525),
        (0.28, 68525, 104425),
        (0.33, 104425, 186475),
        (0.35, 186475, income)
    ]

elif status == 3:  # For the Head of household
    brackets = [
        (0.10, 0, 11950),
        (0.15, 11950, 45500),
        (0.25, 45500, 117450),
        (0.28, 117450, 190200),
        (0.33, 190200, 372950),
        (0.35, 372950, income)
    ]

else:
    print("Invalid filing status!")
    exit()


# Next line is calculate the tax
tax = calculate_tax(income, brackets)

# Display the result
print(f"\nTotal tax owed is: ${tax:.2f}")
#End of program....i believe this can be easily undestood due to the help of the comments
