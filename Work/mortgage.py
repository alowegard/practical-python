# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 2000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > payment:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid += payment 
    
    if month <= extra_payment_end_month and month >= extra_payment_start_month and principal >= extra_payment:
        principal = principal - extra_payment
        total_paid += extra_payment
    
    print(month, round(total_paid,2), round(principal,2))

if principal > 0:
    month += 1
    total_paid += principal
    print(month, round(total_paid,2), 0.0)

