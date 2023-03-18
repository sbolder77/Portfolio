def recursive_sum(my_num):
    """Calculates and returns the sum of all numbers between 0 and the 'n' parameter"""
    if my_num == 0:
        return 0
    else:
        return(my_num + recursive_sum(my_num-1))

def list_sum(my_num_list):
    """Adds all the numbers in the [] and returns the total value"""
    if len(my_num_list) == 1:
        return my_num_list[0]
    else:
        return my_num_list[0] + list_sum(my_num_list[1:])

def bunny_ears(my_bunnies):
    """takes the num_of_bunnies and returns the total number of ears (2 per bunny)"""
    if my_bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(my_bunnies - 1)

def reverse_string(my_str):
    """Takes a string and returns the string in reverse"""
    if len(my_str) == 0:
        return my_str
    else:
        return reverse_string(my_str[1:]) + my_str[0]

def get_max(my_nums):
    
    if len(my_nums) == 1:
        return my_nums[0]
    else:
        return max(my_nums[0], get_max(my_nums[1:]))

def main():
    print("The result of the recursive_sum function is -", str(recursive_sum(5)))
    print("The result of the list_sum function is -", str(list_sum([10, 12.5, 10, 7])))
    print("The number of bunny ears is -", bunny_ears(10))
    print("The reverse string is -", reverse_string("cat"))
    print("The max number of my list of numbers is -", get_max([11,22,3,41,15]))

if __name__ == '__main__':
    main()