import sys

try:
    salary = int(sys.argv[1])

    Taxable_income = salary - 5000
    if Taxable_income>0 :
        if Taxable_income <= 3000:
            Tax = format(Taxable_income * 0.03,".2f")
        elif Taxable_income > 3000 and Taxable_income <= 12000:
            Tax = format(Taxable_income * 0.1 -210,".2f")
        elif Taxable_income > 12000 and Taxable_income <= 25000:
            Tax = format(Taxable_income * 0.2 - 1410,".2f")
        elif Taxable_income > 25000 and Taxable_income <= 35000:
            Tax = format(Taxable_income * 0.25 - 2660,".2f")
        elif Taxable_income > 35000 and Taxable_income <= 55000:
            Tax = format(Taxable_income * 0.3 - 4410,".2f")
        elif Taxable_income > 55000 and Taxable_income <= 80000:
            Tax = format(Taxable_income * 0.35 - 7160,".2f")
        else:
            Tax = format(Taxable_income * 0.45 - 15160,".2f")

        print(Tax)
    else:
        print(format(0,".2f"))

except ValueError as error:
    print("Parameter Error")