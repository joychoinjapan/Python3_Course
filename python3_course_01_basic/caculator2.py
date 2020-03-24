import sys


def calculate(salary):
        salary=int(salary)
        yanglao=0.08
        yiliao=0.02
        shiye=0.005
        gongjijin=0.06
        discount=yanglao+yiliao+shiye+gongjijin
        Taxable_income = salary*(1-discount)- 5000
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

            take_home_pay=format(salary*(1-discount)-float(Tax),".2f")
        else:
            take_home_pay=format(salary*(1-discount),".2f")
        return  take_home_pay



output_dict={}
for item in sys.argv[1:]:
    try:
        item = item.split(':')
        output_dict[item[0]] = item[1]
        take_home_pay=calculate(item[1])
        print(item[0]+":"+take_home_pay)
    except (ValueError, TypeError):
        print("Parameter Error")

