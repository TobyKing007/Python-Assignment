principal = float(input("Enter loan amount: "))

annual_interest_rate = float(input("Enter interest rate: "))

duration = float(input("Enter loan duration: "))

monthly_rate = annual_interest_rate /100 / 12

number_of_months = duration * 12

monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** number_of_months) / ((1 + monthly_rate) ** number_of_months - 1)

print ("The monthly mortgage payment is: ", monthly_payment)
