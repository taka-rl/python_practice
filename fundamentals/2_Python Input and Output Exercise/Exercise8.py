'''

'''

totalMoney = 1000
quantity = 3
price = 450
print("I have", totalMoney, "dollars so I can buy", quantity, "football for", price, "dollars")

line = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars".format(totalMoney, quantity, price)
print(line)

#format grammar
#string({0} ***** {1:.3d/.2f}).format(*, **, ***, .....)
#if you want to modifiy the digit of floating number, {indext number:.桁d/f}
