SALES_FILE = 'sales.txt'


class Employee:

    def __init__(self, hourly: float) -> None:
        self.hours = 0
        self.rate = hourly

    def get_hours(self):
        return self.hours
    
    def set_hours(self, hours: float):
        try:
            self.hours = float(hours)
        except:
           print("Invalid data type used to set hours")
    
    def get_pay(self):
        return self.rate

    def set_pay(self, rate: float):
        try:
            self.rate = float(rate)
        except:
           print("Invalid data type used to set rate")


class CoffeeShop:

    def __init__(self, name='', drinkDict=dict()) -> None:
        self.name = name
        self.total_sold = 0
        self.costs = 0
        self.drinks = drinkDict
    
    def add_sale(self, drink: str):
        self.costs += (self.drinks[drink]) / 3
        self.total_sold += self.drinks[drink]
    
    def print_menu(self):
        print('....................')
        for drink in self.drinks:
            print(drink + "....$" + str(round(self.drinks[drink], 2)))
        print('....................')
    
    def compute_profits(self, employees: list):
        salaries = 0
        for emp in employees:
            salaries += emp.get_hours() * emp.get_pay()
        
        return self.total_sold - self.costs - salaries


def read_sales(file: str):
    try:
        with open(file, 'r') as sales:
            cleaned = []
            for sale in sales.readlines():
                cleaned.append(sale.strip())
            return cleaned
    except FileNotFoundError:
        print('File not found, check directory of script')


def main():
    e1 = Employee(12.75)
    e1.set_hours(10)
    e2 = Employee(10.45)
    e2.set_hours(8)
    e3 = Employee(7.50)
    e3.set_hours(4)

    emps = [e1, e2, e3]

    drinks = {
        'Green Tea': 3.25,
        'Black Tea': 3.45,
        'House Coffee': 4.20,
        'Expresso': 4.35,
        'Americano': 5.25,
        'Fruit Smoothie': 8.25
    }

    shop = CoffeeShop("Charlie's", drinks)

    shop.print_menu()
    sales = read_sales(SALES_FILE)

    for sale in sales:
        shop.add_sale(sale)
    
    print("Daily profit: $" + str(round(shop.compute_profits(emps), 2)))


main()
