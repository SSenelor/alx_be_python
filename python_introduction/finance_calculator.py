#Get user input
monthly_income_str = input("Enter your monthly income: " )
monthly_expenses_str = input("Enter your total monthly expenses: " )

monthly_income_int = int(monthly_income_str)
monthly_expenses_int = int(monthly_expenses_str)

#Calculations
monthly_savings = monthly_income_int - monthly_expenses_int

# Calculate Projected Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print Result
print("Your monthly savings are", monthly_savings,".")
print("Projected savings after one year, with interest, is:", projected_savings)