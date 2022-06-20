#!/usr/bin/env python

# pcost.py
#
# Exercise 1.27


import csv
import sys
import report

def portfolio_cost(filename):
    total = 0.0
    portfolio = report.read_portfolio(filename)
    for rowno, stock in enumerate(portfolio,1):
        try:
            stockNum = stock.shares
            stockCost = stock.price
            total += stockNum*stockCost
        except ValueError:
            print(f'Entry {rowno}: Bad entry: {row}')            
    return total

def main(argv):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print(f'Total stock price is ${cost:0,.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)
