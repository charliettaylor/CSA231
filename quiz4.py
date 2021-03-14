# Quiz 4: City Projections by Charlie Taylor

FILE_NAME = 'localpops.txt'


def import_cities(fileName: str) -> list:
    '''
    opens file of name specified by parameter and cleans data to be returned
    in a list of lists
    '''
    try:
        cities = open(fileName)

        parse = cities.readlines()
        cleaned_data = []

        for city in parse:
            cleaned_data.append(city.strip().split(', '))

        cities.close()
        return cleaned_data
    except FileNotFoundError:
        print("File ", fileName, "not found")
        return None


def print_intro(cities: list) -> None:
    '''
    prints opening to program
    '''
    print("-" * 34)
    print("City Projections by Charlie Taylor")
    print("-" * 34)
    print("The cities in our available data set:")
    for idx, city in enumerate(cities):
        print(idx, '-', city[0])


def handle_input() -> list:
    '''
    asks for input and keeps asking until valid input is given
    '''
    userCity = int(input("Please enter your city: "))
    while userCity < 0:
        userCity = int(input("Invalid input. Please enter your city: "))

    userPop = int(input("Enter the starting population: "))
    while userPop < 0:
        userCity = int(input("Invalid input. Enter the starting population: "))

    userYears = int(input("Enter number of years: "))
    while userYears < 1:
        userCity = int(input("Invalid input. Enter number of years: "))

    return [userCity, userPop, userYears]


def calculate_and_print(cities: list, userData: list) -> list:
    '''
    calculates the net change per year of the city and then prints each year's
    total population
    returns a list with the name of the city at idx 0 and the projections after
    '''
    city = userData[0]
    net_change = -1 * int(cities[city][1]) + int(cities[city][2]) +\
        int(cities[city][3])
    totalPop = userData[1]

    output = [cities[city][0]]

    for year in range(1, userData[2] + 1):
        totalPop += net_change
        output.append([year, totalPop])
        print(year, totalPop)

    return output


def pop_projection_file(output: list) -> None:
    '''
    creates new file and writes the user's prediction choice to it
    '''
    fileName = output[0].replace(' ', '_').lower()
    out = open(fileName + '_pop_projection.txt', "w+")
    output.pop(0)
    for year in output:
        out.write(str(year[0]) + ", " + str(year[1]) + "\n")
    out.close()


def main():
    cities = import_cities(FILE_NAME)
    if cities is None:
        print("Please add the", FILE_NAME, "to the directory")
    else:
        print_intro(cities)
        cont = 'Y'
        while cont == 'Y':
            userData = handle_input()
            output = calculate_and_print(cities, userData)
            pop_projection_file(output)
            cont = input("Would you like to continue? (Y/N)").upper()


if __name__ == "__main__":
    main()
