from datetime import datetime
from datetime import date

class UnsortedTransaction(object):
    date = date.min
    amount = 0
    location = ""

    def __init__(self, date, amount, location):
        self.date = date
        self.amount = amount
        self.location = location

def main():
    date = datetime.strptime("09/20/2018", "%m/%d/%Y").date()

    transaction = UnsortedTransaction(
        date,
        -7.34,
        "Alberto's"
    )

    print(transaction.date)
    print(transaction.amount)
    print(transaction.location)

if __name__ == "__main__":
    main()