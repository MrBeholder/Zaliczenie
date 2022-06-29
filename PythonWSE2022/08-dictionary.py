price = {'Pb95':6.64, 'Pb98':6.80, 'ON':6.88, 'LPG':3.29}
cash = float(input("Za ile zatankować?"))
for key, value in price.items():
    print(key, value, "zł, -", round(cash/value,2), "l")

# price['LPG'] = 2.30
# print(price)
# price['AdBlue'] = 11.22
# print(price)