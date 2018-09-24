from sortedtransaction import *
from datetime import datetime
import unittest

class UnsortedTransactionTest(unittest.TestCase):
    sortedTransaction = SortedTransaction(
        Category.SAVINGS,
        datetime.today().date(),
        0.00,
        ""
    )

    def test_category(self):
        self.assertEqual(self.sortedTransaction.category,
            Category.SAVINGS
        )