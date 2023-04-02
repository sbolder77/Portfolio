'''This is a code example related to classes, objects and methods, how they are defined and how to work with the objects
Simon Bolder 01/03/2023
'''

#region Classes
class Person:
    count = 0
    '''Represents a generic person'''
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):
        '''Returns the BMI of a person'''
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2
    
    @classmethod
    def print_count(cls,):
        '''Returns the person count in the class'''
        return cls.count

    def print_self(self):
        '''Returns the personal details of the person'''
        return (self.first_name, self.last_name, self.weight_in_lbs, self.height_in_inches)
#endregion

def main():
    p = Person('Tom', 'Thumb', 150, 62)
    p2 = Person('Fred', 'Flint', 225, 57)
    
    '''Calls for the person class methods'''
    print(p.calc_bmi())
    print(p2.calc_bmi())
    print(Person.print_count())
    print(Person.print_self(p))

if __name__ == '__main__':
    main()