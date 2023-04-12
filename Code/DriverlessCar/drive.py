'''module to calculate speed and battery status of driverless car'''
import random

#region constants
RESIDENTIAL_SPEED = 30
NATIONAL_SPEEDS = [40, 50, 60, 70]
#endregion

#region class
class Speed:
    '''class to represent the speed and power for a vehicle'''
    def __init__(self):
        '''initialises the charge state'''
        self.charge = False

    def get_speed(self, zone):
        '''returns speed for car'''
        if zone == 'R':
            return RESIDENTIAL_SPEED
        else:
            return random.choice(list(NATIONAL_SPEEDS))

    def get_charge_status(self):
        '''returns battery charge'''
        return self.charge

    def set_charge_status(self, charge):
        '''returns the battery status'''
        if charge == 'Y':
            return 'Battery is charged'
#endregion
