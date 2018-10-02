import sys
import random
from unsortedtransaction import UnsortedTransaction
from sortedtransaction import SortedTransaction
from sortedtransaction import Category

class CSVManager(object):

    def __init__(self, csvfile_in, csvfile_out):
        self.csvfile_in = csvfile_in
        self.csvfile_out = csvfile_out
        self.unsorted_transactions = []
        self.sorted_transactions = []

    def csvfile_in_to_transactions(self):
        file = open(self.csvfile_in, "r")
        for line in file.readlines():
            attributes = line.split(",")
            self.unsorted_transactions.append(
                UnsortedTransaction(attributes[0].strip(),
                attributes[1].strip(),
                attributes[4].strip())
            )
        file.close()

    def sort_transaction(self, category):
        unsorted_transaction = self.unsorted_transactions[0]
        self.unsorted_transactions.remove(unsorted_transaction)
        self.sorted_transactions.append(SortedTransaction(
            category,
            unsorted_transaction.date,
            unsorted_transaction.amount,
            unsorted_transaction.location
        ))

    def transactions_to_csvfile_out(self):
        file = open(self.csvfile_out, "w")
        for sorted_transaction in self.sorted_transactions:
            file.write(",%s,%s,%s,%s\n" %
            (sorted_transaction.category.name,
            sorted_transaction.amount,
            sorted_transaction.location,
            sorted_transaction.date))
        file.close()


def main():
    csvmanager = CSVManager("transactions_914_921.csv", "testoutput.test")
    csvmanager.csvfile_in_to_transactions()
    csvmanager.sort_transaction(Category(random.randint(0,9)))
    csvmanager.transactions_to_csvfile_out()

if __name__ == "__main__":
    main()
