from unsortedtransaction import UnsortedTransaction
from datetime import datetime
import unittest

class UnsortedTransactionTest(unittest.TestCase):
    transaction = UnsortedTransaction(
        datetime.today().date(),
        0.00,
        ""
        )

    def setUp(self):
        self.transaction = UnsortedTransaction(
            datetime.strptime("09/20/2018", "%m/%d/%Y").date(),
            -7.34,
            "Alberto's"
        )

    def test_date(self):
        self.assertEqual(self.transaction.date.month, 9)
        self.assertEqual(self.transaction.date.day, 20)
        self.assertEqual(self.transaction.date.year, 2018)

    def test_amount(self):
        self.assertEqual(self.transaction.amount, -7.34)

    def test_location(self):
        self.assertEqual(self.transaction.location, "Alberto's")

if __name__ == "__main__":
    unittest.main()