'''Script to utilise basic CLI/Shell commands'''
import os

def shell_path():
    """Prints the contents of the current working directory"""
    print(os.listdir(os.getcwd()))
    
def shell_add():
    """Prints the addtion of 2 numeric values"""
    num1 = int(input("Please enter number 1: "))
    num2 = int(input("Please enter number 2: "))
    print(num1 + num2)

def shell_help():
    """Prints simple text about the python shell help"""
    print("""psh: shell implementation in Python.
          Supports all basic shell commands.""")

def main():
    """Executes functions based on input"""
    while True:
        inp = input("Please enter command in capitals - LIST/ADD/HELP/EXIT: ")
        if inp == "LIST":
            shell_path()
        elif inp == "ADD":
            shell_add()
        elif inp == "HELP":
            shell_help()
        elif inp == "EXIT":
            break

if __name__ == '__main__':
    main()
