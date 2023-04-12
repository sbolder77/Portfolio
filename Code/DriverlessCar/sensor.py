'''module represents a small number of possible simulated alerts including vehicles and traffic lights'''
import random

#region constants
MOTORWAY_ALERTS = ['car', 'lorry']
RESIDENTIAL_ALERTS = ['red', 'green', 'car', 'bike']
RESIDENTIAL_ALERT_SPEEDS = [2.0, 3.5]
MOTORWAY_ALERT_SPEEDS = [6.0, 8.0, 13.0, 15.0]
#endregion

#region class
class Sensors:
    '''class to represent sensors on a car'''
    def get_alerts(self, zone, miles, speed):
        '''provides values back to the car based on the parameters and the constant variables'''
        __alerts = []
        if zone == 'R':
            if (miles >= RESIDENTIAL_ALERT_SPEEDS[0] and miles <= RESIDENTIAL_ALERT_SPEEDS[1]) and speed == 30:
                __alert = random.choice(list(RESIDENTIAL_ALERTS))
                if __alert == 'red':
                    __alerts.append(0)
                    __alerts.append(__alert)
                if __alert == 'green':
                    __alerts.append(30)
                    __alerts.append(__alert)
                if __alert == 'car':
                    __alerts.append(speed - 5)
                    __alerts.append(__alert)
                if __alert == 'bike':
                    __alerts.append(speed - 10)
                    __alerts.append(__alert)
        else:
            if (miles >= MOTORWAY_ALERT_SPEEDS[0] and miles <= MOTORWAY_ALERT_SPEEDS[1]) and speed > 30:
                __alert = random.choice(list(MOTORWAY_ALERTS))
                if __alert == 'car':
                    __alerts.append(speed - 5)
                    __alerts.append(__alert)
                if __alert == 'lorry':
                    __alerts.append(speed - 10)
                    __alerts.append(__alert)
            if (miles >= MOTORWAY_ALERT_SPEEDS[2] and miles <= MOTORWAY_ALERT_SPEEDS[3]) and speed > 30:
                __alert = random.choice(list(MOTORWAY_ALERTS))
                if __alert == 'car':
                    __alerts.append(speed - 10)
                    __alerts.append(__alert)
                if __alert == 'lorry':
                    __alerts.append(speed - 15)
                    __alerts.append(__alert)
        return __alerts

#endregion
