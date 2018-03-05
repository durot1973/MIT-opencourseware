#We are getting the necessary variables
annual_salary = int(input('Enter you starting annual salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0
r = 0.04
monthly_salary = annual_salary/12

multiples = []
for i in range(0,100000, 6):
    multiples.append(i)
del multiples[0]
print(multiples)

#here we initiate the variables in a while loop to get the down payment
while current_savings < portion_down_payment:
    monthly_intrest = current_savings*r/12   #monthly_intrest is the money every month on intrest on savings
    current_savings += monthly_intrest
    current_savings += (portion_saved * monthly_salary)
    months += 1
    if months in multiples:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        monthly_salary = annual_salary/12