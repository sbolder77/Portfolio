'''Module with function to calculate moves and print'''
runcount = 0 

def Hanoi(n, src, dst, tmp):
    if n > 0:
        global runcount
        runcount += 1 
        Hanoi(n - 1, src, tmp, dst)
        print ("Moved disc", chr(64 + n), "From tower", src, "to tower", dst)
        Hanoi(n - 1, tmp, dst, src)

disks = int(input('Enter the number of disks: '))

Hanoi(disks,0,2,1)

print('Moved: ' + str(runcount) + ' times')