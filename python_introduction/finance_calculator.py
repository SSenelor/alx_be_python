#Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculations
monthly_savings = monthly_income - monthly_expenses

# Calculate Projected Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print Result
print("Your monthly savings are", monthly_savings,".")
print("Projected savings after one year, with interest, is:", projected_savings)
