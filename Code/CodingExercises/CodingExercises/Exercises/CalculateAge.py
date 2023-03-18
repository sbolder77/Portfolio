'''This is a code example related to calculating Age and uses public and private variables
Simon Bolder 01/03/2023'''

from datetime import date

'''The while statements were added to force the user to enter the correct values.'''
while True:
    try:
        birth_Day = int(input('Enter your birth day (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

while True:
    try:
        birth_Month = int(input('Enter your birth month (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

while True:
    try:
        birth_Year = int(input('Enter your birth year (numeric): '))
        break
    except ValueError:
        print("Please input integer only...")
        continue

birth_Name = input('Enter your name: ')

class Age:
    '''Added the class to hold a function to return the users age in years.'''
    def __init__(self, day, month, year, name):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        self.name = name.upper()
    
    def ageData(self):
        _today = date.today()
        _age = _today.year - self.year - ((_today.month, _today.day) < (self.month, self.day))
        print(self.name + " - you are: " + str(_age) + " years old")

def main():
    my_Age = Age(birth_Day, birth_Month, birth_Year, birth_Name)
    my_Age.ageData()

if __name__ == '__main__':
    main()
