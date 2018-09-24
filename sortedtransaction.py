from datetime import datetime
import unsortedtransaction
from enum import Enum


class Category(Enum):
    FIXED_BILLS = 0
    UTILITIES = 1
    GROCERIES = 2
    GASS = 3
    CAR = 4
    FUN = 5
    STUFF = 6
    VACATION = 7
    DATE = 8
    SAVINGS = 9

class SortedTransaction(unsortedtransaction.UnsortedTransaction):

    category = Category.FIXED_BILLS

    def __init__(self):
        self.category = Category.FIXED_BILLS
        unsortedtransaction.UnsortedTransaction.__init__(self)

    def __init__(self, category, date, amount, location):
        self.category = category
        unsortedtransaction.UnsortedTransaction.__init__(
            self,
            date,
            amount,
            location
            )

def main():

    date = datetime.strptime("09/20/2018", "%m/%d/%Y").date()

    sorted_transaction = SortedTransaction(
        Category.SAVINGS,
        date,
        -7.34,
        "Alberto's"
    )

    print(sorted_transaction.category)
    print(sorted_transaction.date)
    print(sorted_transaction.amount)
    print(sorted_transaction.location)

if __name__ == "__main__":
    main()