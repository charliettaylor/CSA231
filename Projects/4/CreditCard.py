
class CreditCard():

    def __init__(self, newBalance=0.0, newLimit=1200.0, newInterest=0.07):
        if newLimit <= 0:
            raise ValueError("Limit must be greater than 0")
        elif newInterest <= 0:
            raise ValueError("Interest must be greater than 0")
        self.balance = float(newBalance)
        self.limit = float(newLimit)
        self.interest = float(newInterest)


    def adjust_limit(self, newLimit) -> None:
        '''
        changes self.limit to new limit, as long as it is positive and >= 
        the current balance
        '''
        if newLimit <= 0:
            raise ValueError("Limit must be greater than 0")
        elif newLimit < self.balance:
            raise ValueError("Limit must be greater than current balance")
        self.limit = newLimit


    def adjust_interest(self, newInterest) -> None:
        '''
        changes interest rate as long as it is positive and nonzero
        '''
        if newInterest <= 0:
            raise ValueError("Interest must be greater than 0")
        self.interest = newInterest


    def get_balance(self) -> float:
        '''
        returns the current balance
        '''
        return self.balance
    

    def make_payment(self, payment) -> bool:
        '''
        reduces balance on card as long as value given in positive
        '''
        if payment <= 0:
            raise ValueError("Payment must be greater than 0")
        self.balance -= payment


    def add_charge(self, charge) -> None:
        '''
        only adds charges to card if charge is positive and does not exceed
        card limit
        '''
        if charge <= 0:
            raise ValueError("Charge must be greater than 0")
        
        if self.balance + charge > self.limit:
            return False
        else:
            self.balance += charge
            return True


    def compute_bill(self, interest: bool) -> float:
        '''
        computes the bill based on interest parameter and rounds
        '''
        if self.interest > 0 and interest:
            return round((1 + self.interest) * self.balance, 2)
        return round(self.balance, 2)


    def __str__(self) -> str:
        string = 'Balance: ' + self.balance + '\nInterest Rate: '\
        + self.interest + '\nCredit Limit: ' + self.limit
        return string

