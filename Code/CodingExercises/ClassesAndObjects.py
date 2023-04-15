'''This is a code example related to classes and objects, how they are defined and how to work with the objects
Simon Bolder 01/03/2023
'''

#region Classes
class Person:
    '''Represents a generic person'''
    def __init__(self, first, last, weight, height):
          self.first_name = first
          self.last_name = last
          self.weight_in_lbs = weight
          self.height_in_inches = height
#endregion

#region objects
'''Instantiating the person class to create new objects'''
p1 = Person('Tom', 'Thumb', 150, 78)
p2 = Person('Tim', 'Thumb', 140, 60)
p3 = Person('Tony', 'Thumb', 130, 50)
p4 = Person('Tanya', 'Thumb', 120, 40)
p5 = Person('Terri', 'Thumb', 110, 30)
#endregion

def main():
    '''Create a new list and add the objects to it'''
    p_list = []
    p_list.append(p1)
    p_list.append(p2)
    p_list.append(p3)
    p_list.append(p4)
    p_list.append(p5)

    '''Printing the objects in the list using object index and attributes'''
    for p in range(len(p_list)):
        print(p_list[p].first_name + ' ' + p_list[p].last_name)

if __name__ == '__main__':
    main()