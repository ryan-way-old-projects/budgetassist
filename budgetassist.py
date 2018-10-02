import sys
from os import system
from csvmanager import CSVManager
from sortedtransaction import Category

def printcategories():
    [print("%s, %s" % (e.name, e.value)) for e in Category]

def print_unsorted_transactions(csvmanager):
    print("\nUnsorted Transactions:")
    [print("%s, %s, %s" % (e.date, e.amount, e.location)) for e in csvmanager.unsorted_transactions]

def print_sorted_transactions(csvmanager):
    print("\nSorted Transactions:")
    [print("%s, %s, %s" % (e.category, e.amount, e.location)) for e in csvmanager.sorted_transactions]


def main():
    csvfile_in = sys.argv[1]
    csvfile_out = sys.argv[2]
    csvmanager = CSVManager(csvfile_in, csvfile_out)
    csvmanager.csvfile_in_to_transactions()
    while len(csvmanager.unsorted_transactions) > 0:
        system("clear")
        printcategories()
        print_unsorted_transactions(csvmanager)
        print_sorted_transactions(csvmanager)
        category = Category(int(input()))
        csvmanager.sort_transaction(category)
    csvmanager.transactions_to_csvfile_out()


if __name__ == "__main__":
    main()