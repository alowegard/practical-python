#!/usr/bin/env python
# report.py
#
# Exercise 2.4

import csv
import fileparse
import stock

def read_portfolio(filename):
    '''
    returns an array of dictionaries containing name, shares, and price for each row of your csv file
    '''
    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header,row))
            mystock = stock.Stock(record['name'], int(record['shares']), float(record['price']))    
            portfolio.append(mystock)
    return portfolio

def read_prices(filename):
    '''
    returns a dictionary of stocks with their corresponding prices from your csv input
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def get_gains(portfolio, prices):
    ''''
    takes as input the output from read_portfolio and read_prices to calculate gains/losses
    '''
    current_value = 0.0
    gain = 0.0
    for d in portfolio:
        gain += (prices[d.name] - d.price)*d.shares
        current_value += d.shares*prices[d.name]
    print("current value = ", f'${current_value:0.2f}', "gain/loss = ", f'${gain:0.2f}')


def make_report(portfolio, prices):
    '''
    takes as input the portfolio and prices output from read_portfolio and read_prices 
    and returns a table with name, shares, price, and change in price
    '''
    report = []
    for d in portfolio:
        change = (prices[d.name] - d.price)
        report.append((d.name, d.shares, prices[d.name], change))
    return report

def print_report(report):
    '''
    takes as input a report from the make_report function and prints out a formatted table
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        price = '$'+'%0.2f' % price
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, price_filename):
    '''
    takes as input the filenames for portfolio and prices and prints out a formatted table of information
    '''
    portfolio = read_portfolio(portfolio_filename)
    with open(price_filename) as file:
        prices = dict(fileparse.parse_csv(file, has_headers=False, types=[str,float]))
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    portfolio_report(argv[1],argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
