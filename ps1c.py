#We are getting the necessary variables
annual_salary = int(input('Enter you starting annual salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12

multiples = []
for i in range(0,100000, 6):
    multiples.append(i)

lowest = 0
highest = 10000
best = ((highest + lowest)/float(2))/10000
bisections = 0

#here we initiate the variables in a while loop to get the down payment
for months in range(36):
    try:
        monthly_intrest = current_savings*r/12 #monthly_intrest is the money every month on intrest on savings
        current_savings += monthly_intrest
        current_savings += (best * monthly_salary)
        if months in multiples:       #This makes increments in his annual salary every six months
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary/12
      
    if abs(current_savings - portion_down_payment) <= 100:
        
    best = ((highest + lowest)/float(2))/float(10000)
    bisections += 1
    if abs(current_savings - portion_down_payment) <= 100:
        print('best savings rate =', best)
        print('number of bisections is ', bisections)
    else:
        print('It is not possible to pay the down payment in three years' )