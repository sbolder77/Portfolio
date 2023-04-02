import random
import statistics

#region variables
'''Source file and answer file variables should be updated for your path in your local source'''
source_file = "C:\\Users\\simon.bolder\OneDrive - Thermo Fisher Scientific\\Documents\\University of Essex\\Portfolio\\Code\\CodingExercises\\Exercises\\text_1_exercise5.txt"
answer_file = "C:\\Users\\simon.bolder\OneDrive - Thermo Fisher Scientific\\Documents\\University of Essex\\Portfolio\\Code\\CodingExercises\\Exercises\\answer_exercise5.txt"
sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']
#endregion

#region exercise1classes
class Lottery:
  def shuffle(self):
    results = []
    for i in range(5):
      results.append(random.randint(1, 20))
    return results

class Powerball(Lottery):
  def shuffle(self):
    '''Overrides the shuffle method and returns a list of six random integers between 1 and 99'''
    results = []
    for i in range(6):
      results.append(random.randint(1, 99))
    return results
#endregion

#region exercise2classes
class Airplane:
  def __init__(self, first_class, business_class, coach):
    pass
    self.first_class = first_class
    self.business_class = business_class
    self.coach = coach

  def total(self):
    '''Return the total number of passengers on board'''
    passengers = self.first_class + self.business_class + self.coach
    return passengers

class Train:
  def __init__(self, car1, car2, car3, car4, car5):
    pass
    self.car1 = car1
    self.car2 = car2
    self.car3 = car3
    self.car4 = car4
    self.car5 = car5

  def total(self):
    '''Return the total number of passengers on board'''
    passengers = self.car1 + self.car2 + self.car3 + self.car4 + self.car5
    return passengers
#endregion

#region exercise3classes
class Characters():
  '''Returns true or false based on the comparison between 2 objects'''
  def __init__(self, list):
    self.phrases = list

  def __gt__(self, other_list):
      if sum(len(w) for w in self.phrases) > sum(len(w) for w in other_list.phrases):
          return "True"
  
  def __lt__(self, other_list):
      if sum(len(w) for w in self.phrases) < sum(len(w) for w in other_list.phrases):
          return "False"

  def __eq__(self, other_list):
      if sum(len(w) for w in self.phrases) == sum(len(w) for w in other_list.phrases):
          return "True"
#endregion

#region exercise4classes
class Median:
    '''calculates the median value of any passed parameters'''
    def calculate_median(self, a = None, b = None, c = None, d = None, e = None):
        if (a is not None and
        b is not None and
        c is not None and
        d is not None and
        e is not None):
            return statistics.median([a,b,c,d,e])
        elif (a is not None and
          b is not None and
          c is not None and
          d is not None):
            return statistics.median([a,b,c,d])
        elif (a is not None and
          b is not None and
          c is not None):
            return statistics.median([a,b,c])
        elif a is not None and b is not None:
            return statistics.median([a,b])
#endregion

#region exercise5classes
class Substitute:
  def __init__(self, source_file, answer_file):
    self.source_file = source_file
    self.answer_file = answer_file
    self.words = None
    
  def string_to_list(self):
    '''Read text file, turn it into a 2D list of words for each line'''
    words = []
    with open(self.source_file, 'r') as file_object:
      lines = file_object.read().split('\n')
      for line in lines:
        words.append(line.split())
    self.words = words
    
  def list_to_string(self):
    '''Convert 2D list back into a string with newline characters'''
    lines = []
    for line in self.words:
      lines.append(' '.join(line))
    string = '\n'.join(lines)
    self.words = string
    text_file = open(self.answer_file, "w")
    text_file.write(string)
  
  def swap_words(self):
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 5 == 0:
          word = line[i]
          line[i] = 'HELLO'
    self.list_to_string()

class Stars(Substitute):
  def swap_words(self):
    '''replaces every 3rd word in the source text with a string of the same length but with * for all characters'''
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 3 == 0:
          word = line[i]
          word_length = len(word)
          new_word = []
          for x in range(word_length):
              new_word.append("*")
          line[i] = ''.join(new_word)
    self.list_to_string()
#endregion

#region functions
def passengers(obj):
  print(f'There are {obj.total()} passengers on board.')
#endregion

#region objects
p_ball = Powerball()
plane = Airplane(30,50,60)
train = Train(2,3,1,5,6)
c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
star = Stars(source_file, answer_file)
m = Median()
#endregion

def main():
    '''Calls for exercise 1'''
    print(p_ball.shuffle())

    '''Calls for exercise 2'''
    passengers(plane)
    passengers(train)

    '''Calls for exercise 3'''
    print(c1 > c2) # prints 'True'
    print(c1 < c2) # prints 'False'
    print(c1 == c1) # prints 'True'

    '''Calls for exercise 4'''
    print(m.calculate_median(3, 5, 1, 4, 2))
    print(m.calculate_median(8, 6, 4, 2))
    print(m.calculate_median(9, 3, 7))
    print(m.calculate_median(5, 2))

    '''Calls for exercise 5'''
    star.swap_words()

if __name__ == '__main__':
    main()