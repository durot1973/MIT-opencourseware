#We are getting the necessary variables
annual_salary = int(input('Enter you annual salary: '))
portion_saved = float(input('Enter the percent of your salary you save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0
r = 0.04
monthly_salary = annual_salary/12

#here we initiate the variables in a while loop to get the down payment
while current_savings < portion_down_payment:
    monthly_intrest = current_savings*r/12   #monthly_intrest is the money every month on intrest on savings
    current_savings += monthly_intrest
    current_savings += (portion_saved * monthly_salary)
    months += 1
print('Number of months:', months )