# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total = 0.0
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for l in rows:
            try:
                stockNum = int(l[1])
                stockCost = float(l[2])
                total += stockNum*stockCost
            except ValueError:
                print("Couldn't parse line: ", l)            
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total stock price is ${cost:0.2f}')
