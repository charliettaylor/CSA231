# Charlie Taylor Project 3

import CreditCard as cc
import unittest as ut


class TestCreditCard(ut.TestCase):
    def setUp(self) -> None:
        self.cc1 = cc.CreditCard()
        self.cc2 = cc.CreditCard(10.0, 5.0, 0.2)

    def test_init(self):
        self.assertRaises(ValueError, cc.CreditCard, 10.0, -5.0, 0.1)
        self.assertRaises(ValueError, cc.CreditCard, 10.0, 5.0, 0.0)

    def test_limit(self) -> None:
        self.cc1.adjust_limit(1000.0)
        self.assertTrue(type(self.cc1.limit), float)
        self.assertTrue(self.cc1.limit, 1000.0)

        self.assertRaises(ValueError, self.cc2.adjust_limit, 0)

    def test_interest(self) -> None:
        self.cc1.adjust_interest(0.1)
        self.assertTrue(type(self.cc1.interest), float)
        self.assertTrue(self.cc1.limit, 0.1)

        self.assertRaises(ValueError, self.cc2.adjust_interest, 0)

    def test_balance_modifiers(self) -> None:
        self.cc1.add_charge(100.0)
        self.assertTrue(type(self.cc1.balance), float)
        self.assertTrue(self.cc1.balance, 100.0)

        self.cc1.make_payment(50.0)
        self.assertTrue(type(self.cc1.balance), float)
        self.assertTrue(self.cc1.balance, 50.0)

        self.assertRaises(ValueError, self.cc2.add_charge, -10)
        self.assertRaises(ValueError, self.cc2.make_payment, -10)

    def runTest(self):
        self.test_init()
        self.test_balance_modifiers()
        self.test_interest()
        self.test_limit()


if __name__ == "__main__":
    ut.main()
