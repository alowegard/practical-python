# tableformat.py

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError() 
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print('%10s' % h, end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print((',').join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print('<tr><th>'+('</th><th>').join(headers)+'</th></tr>')
    
    def row(self, rowdata):
        print('<tr><td>'+'</td><td>'.join(rowdata)+'</td></tr>')

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    Returns the correct TableFormatter object based on user input: txt, csv, or html.
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}') 

def print_table(portfolio, columns, formatter):
    '''
    Prints a table only containing the relevant columns provided.
    '''
    formatter.headings(columns)
    for stocks in portfolio:
        myrow = [ str(getattr(stocks, c)) for c in columns ]
        formatter.row(myrow)

