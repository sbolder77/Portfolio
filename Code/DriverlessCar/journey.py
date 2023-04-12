'''module to represent journey details and calculations on elapsed time, distance etc.'''
from datetime import datetime

#region constants
JOURNEY_DETAILS = {
    "start": "Start Avenue, Startington, ST1 2RT",
    "finish": "Finish Lane, Finishster, FI3 4SH",
    "distance": 20.0
}
#endregion

#region class
class JourneyDetails:
    '''class with function to return and calculate values'''
    def __init__(self):
        '''class to represent the details of a journey'''
        self.start_time = datetime.now()
        self.charge = False
        self.elapsed_mins = 0
        self.miles_covered = 0

    def get_start_time(self):
        '''returns the start time'''
        return self.start_time

    def get_start_address(self):
        '''returns the start address'''
        return JOURNEY_DETAILS["start"]

    def get_finish_address(self):
        '''returns the start address'''
        return JOURNEY_DETAILS["finish"]

    def get_distance(self):
        '''returns the journey distance'''
        return JOURNEY_DETAILS["distance"]

    def set_elapsed_minutes(self, minstoadd):
        '''updates journey elapsed minutes'''
        self.elapsed_mins = self.elapsed_mins + minstoadd

    def get_elapsed_minutes(self):
        '''returns the elapsed minutes'''
        return self.elapsed_mins

    def get_miles_covered(self):
        '''returns the miles covered'''
        return self.miles_covered

    def set_miles_covered(self, speed, time):
        '''sets the miles covered'''
        self.miles_covered = round(self.miles_covered + ((speed / 60) * time),1)

    def get_res_miles(self):
        '''returns a calculated number of the total journey miles'''
        return JOURNEY_DETAILS["distance"] / 4
#endregion
