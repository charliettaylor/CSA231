import unittest


class CreditCard(unittest.TestCase):

    def __init__(self, newBalance=0.0, newInterest=0.0) -> None:
        self.balance = newBalance
        self.limit = 1200.0
        self.interest = newInterest
        self._testMethodName = "test_limit"
        self._cleanups = ''

    def adjust_limit(self, newLimit) -> None:
        self.limit = newLimit

    def test_limit(self) -> None:
        self.assertTrue(type(self.limit), float)

    def adjust_interest(self, newInterest) -> None: 
        self.interest = newInterest

    def test_interest(self) -> None:
        self.assertTrue(type(self.interest), float)

    def get_balance(self) -> float:
        return self.balance
    
    def test_balance(self) -> None:
        self.assertTrue(type(self.balance), float)

    def make_payment(self, payment) -> None:
        self.balance -= payment

    def add_charge(self, charge) -> None:
        self.balance += charge

    def compute_bill(self, interest: bool) -> float:
        if interest:
            return round((1 + self.interest) * self.balance, 2)
        else:
            return round(self.balance, 2)

    def __str__(self) -> str:
        string = 'Balance: ' + self.balance + '\nInterest Rate: '\
        + self.interest + '\nCredit Limit: ' + self.limit
        return string


if __name__ == "__main__":
    unittest.main()
