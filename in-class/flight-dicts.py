import ast

FILENAME = 'small_flightdict.txt'


def welcome() -> None:
    '''
    welcomes user with intro to program
    '''
    print('---------------------------------------------------')
    print('Welcome to the Flight Coordinator by Charlie Taylor')
    print('---------------------------------------------------')


def get_data() -> dict:
    '''
    retrieves dictionary from txt file as specified by global constant
    '''
    try:
        data = open(FILENAME)
        contents = data.read()
        newDict = ast.literal_eval(contents)
    except FileNotFoundError:
        print("Please put file into directory.")
    data.close()
    return newDict


def print_all_codes(flights: dict) -> None:
    '''
    prints all available airports to start from
    '''
    print("Here are all available airports:")
    for key in flights:
        print(key)


def print_destinations(flights: dict, code: str) -> None:
    '''
    prints all destinations that are available from given starting airport
    '''
    print('Here are all available destinations:')
    for city in flights[code]:
        if len(city[0]) > 1:
            print(city[0])


def user_input_start(flights: dict) -> str:
    '''
    takes user input for the starting airport code and returns it
    '''
    userIn = input('What airport code would you like to look at?')
    while userIn not in flights.keys():
        print('Code not recognized, try again.')
        userIn = input('What airport code would you like to look at?')
    return userIn


def check_input(userIn: str, flights: dict, start: str) -> bool:
    '''
    checks to makes sure user inputted an appropriate airport code for
    user_input_end
    '''
    for dest in flights[start]:
        if userIn in dest and len(userIn) == 3:
            return False
    return True


def lowest_costs_inorder(flights: dict, start: str, end: list) -> None:
    '''
    prints flights in ascending order by price from end: list
    '''
    order = []
    for place in end:
        for dest in flights[start]:
            if place in dest:
                order.append(dest[-1])
    for idx, price in enumerate(sorted(order)):
        print(end[idx], 'average flight cost is $' + price)


def user_input_end(flights: dict, start: str, n) -> list:
    '''
    takes user inputs for the destination airport code and returns a list
    only allows either n amount of flight codes or max amount of destinations
    '''
    inputs = []
    while len(inputs) < min(len(flights[start]) - 1, n):
        userIn = input('What flight price would you like to look at?')
        invalid = check_input(userIn, flights, start)
        while invalid:
            print('Code not recognized, try again.')
            userIn = input('What flight price would you like to look at?')
            invalid = check_input(userIn, flights, start)
        inputs.append(userIn)

    return inputs


def single_or_multiple() -> int:
    '''
    asks how many flights the user wants to check, returns the number
    '''
    choice = int(input('Check the price of [1] or [n] flights?'))

    while not choice > 0 and not type(choice) == int:
        choice = int(input("Please enter valid input."))
    return choice


def main():
    welcome()
    flights = get_data()

    print_all_codes(flights)
    start = user_input_start(flights)

    print_destinations(flights, start)

    choice = single_or_multiple()
    end = user_input_end(flights, start, choice)
    lowest_costs_inorder(flights, start, end)


def test():
    '''
    test version of main to check where errors are
    '''
    welcome()
    flights = get_data()
    assert type(flights) == dict
    print_all_codes(flights)
    start = user_input_start(flights)
    assert type(start) == str and len(start) == 3
    print_destinations(flights, start)
    choice = single_or_multiple()
    assert type(choice) == int and choice > 0
    end = user_input_end(flights, start, choice)
    assert type(end) == str and len(end) == 3
    lowest_costs_inorder(flights, start, end)

if __name__ == '__main__':
    main()
