# invest.py

# Track growing amount of an investment overtime
# Define function for computing the Future Value

def invest(amount, rate, no_years):
    FV = amount * pow((1 + rate),no_years)
    return FV

# Create input parameters

amount = float(input(" Enter Pincipal Amount: "))
rate = float(input(" Enter Annual Rate of Return in %: "))
no_years = int(input(" Enter no. of years: "))
i= no_years

# Print Future Value of investment for each specified number of years in 2 decimal places

for i in range(1,no_years+1):
    Future_Value=invest(amount, rate, i)
    print(f"year {i}: ${Future_Value:,.2f}")
