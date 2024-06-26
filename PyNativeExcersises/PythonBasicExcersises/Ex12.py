"""
Exercise 12: Calculate income tax for the given income by adhering to the rules below

Taxable Income	    Rate (in %)
First $10,000	         0
Next $10,000	        10
The remaining	        20

"""

def tax_income(income) :
    if income < 10000:
        print("yo are poor no need for tax bro")

    elif income <= 20000:
        taxable = income * 10 / 100
        after_tax = income - taxable
        print(f"you have 10% tax bro, total for ya : {after_tax}")

    elif income > 20000:
        tax_payable = 0

        # next 10,000 10% tax
        tax_payable = 10000 * 10 / 100
        # remaining 20% tax

        tax_payable += (income - 20000) * 20 / 100

        income -= tax_payable

        print(f"damn you rich you paid more tax {income}")


tax_income(45000)
