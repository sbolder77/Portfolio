'''This is a code example related to calculating speed to be used in a project for an autonomous car
Simon Bolder 01/03/2023
'''

#region constants
'''Constant variables to be used in the class and getSpeedInfo functions.'''
LOWEST_RES_SPEED = 28
HIGHEST_RES_SPEED = 32
RESIDENTIAL_SPEED_LIMIT = 30
NATIONAL_SPEED_LIMIT = 70
#endregion

#region variables
_current_speed = 25
#endregion

#region classes
class speed_limit:
    '''Returns message if car exceeds national speed limit based on call from getSpeedInfo().'''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def fact(self):
        return "Exceeding the national speed limit"

class residential(speed_limit):
    '''Returns message if car is within residentisl speed limits based on call from getSpeedInfo().'''
    def __init__(self, speed):
        super().__init__("Residential")
        self.speed = speed
        
    def fact(self):
        if self.speed < LOWEST_RES_SPEED:
           return "Speed is well below the residential speed limit - " + str(self.speed) + "mph"
        if self.speed > LOWEST_RES_SPEED or self.speed < HIGHEST_RES_SPEED:
            return "Speed is within the allowed speed limit - " + str(self.speed) + "mph"

class national(speed_limit):
    '''Returns message if car is within residential and national speed limits based on call from getSpeedInfo().'''
    def __init__(self, speed):
        super().__init__("National")
        self.speed = speed

    def nationalSpeed(self):
        return "Speed is within residential and national speed limit - " + str(self.speed) + "mph"
#endregion

#region functions
def getSpeedInfo(vehicle_speed):
    '''Compares the cars current speed against the 
    constant variables to determine the class type and will print a return message from the class.'''

    _residential_speed = residential(vehicle_speed)
    _national_speed = national(vehicle_speed)
    _excess_speed = national(vehicle_speed)

    if vehicle_speed > LOWEST_RES_SPEED and vehicle_speed < HIGHEST_RES_SPEED:
        print(_residential_speed.fact())
    else:
        if vehicle_speed < LOWEST_RES_SPEED:
            print(_residential_speed.fact())

    if vehicle_speed > RESIDENTIAL_SPEED_LIMIT and vehicle_speed < NATIONAL_SPEED_LIMIT:
        print(_national_speed.nationalSpeed())
    else:
        if vehicle_speed > NATIONAL_SPEED_LIMIT:
            print(_excess_speed.fact())
#endregion

def main():
    getSpeedInfo(_current_speed)

if __name__ == '__main__':
    main()
