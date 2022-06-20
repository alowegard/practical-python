# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a list of lines into a list of records
    '''
    # Raise an exception if select and has_headers=False is passed
    if select and not has_headers:
        raise RuntimeError("You must provide a header if you provide types.")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers if they exist
    if has_headers:
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries.
    if select:
        indices = [headers.index(colname) for colname in select ]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:
            continue
        # Filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices ]
        # Apply the provided types to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    print(f'There is an issue with row {rowno}: {row}')
                    print(f'Reason: {e}')
                continue

        # Make a dictionary only if there is a header present, otherwise make the row into a tuple.
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
