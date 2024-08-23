'''
Exercise 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
'''

def calincome(num):
    income = num
    
    if income <= 10000:
        return 10000 * 0
    
    if income <= 20000:
        return (income - 10000) * 0.1
    
    if income > 20000:
        return 10000 * 0.1 + (income - 20000) * 0.2

print("Expected Output:", calincome(12000))

#--------sample answer------
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 0 / 100
    tax_payable += (income -20000) * 20 / 100
