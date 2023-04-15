#region functionsExercise1
def recursive_sum(n):
    '''Calculates and returns the sum of all numbers between 0 and the 'n' parameter'''
    if n == 0:
        return 0
    else:
        return(n + recursive_sum(n-1))
#endregion

#region functionsExercise2
def list_sum(list):
    '''Return the sum of all of the numbers in the list'''
    for num in list:
        if num == 0:
            return 0
        else:
            return sum(list)
#endregion

#region functionsExercise3
def bunny_ears(num_of_bunnies):
    '''Return the number of bunny ears (2 per bunny)'''
    if num_of_bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(num_of_bunnies - 1)
#endregion

#region functionsExercise4
def reverse_string(my_str):
    '''Return the string in reverse order'''
    if len(my_str) == 0:
        return my_str
    else:
        return reverse_string(my_str[1:]) + my_str[0]
#endregion

#region functionsExercise5
def get_max(my_nums):
    '''Return the largest number in the list'''
    if len(my_nums) == 0:
        return 0
    else:
        return max(my_nums[0], get_max(my_nums[1:]))
#endregion

def main():
    print(recursive_sum(10))
    print(list_sum([1,2,3,4,5]))
    print(bunny_ears(8))
    print(reverse_string("house"))
    print(get_max([1,2,3,4,5]))

if __name__ == '__main__':
    main()