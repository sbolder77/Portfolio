from datetime import date, datetime

#region Constants
START_TIME = datetime
CHARGE = bool
JOURNEY_DETAILS = {
    "start": "Start Avenue, Startington, ST1 2RT",
    "finish": "Finish Lane, Finishster, FI3 4SH"
}
TOTAL_JOURNEY_DISTANCE = 60
#endregion

#region class
class JourneyDetails:
    ''''''
    def __init__(self):
        self.startTime = datetime.now()
        self.charge = False
        self.start_address = JOURNEY_DETAILS["start"]
        self.finish_address = JOURNEY_DETAILS["finish"]
        self.total_distance = TOTAL_JOURNEY_DISTANCE
    
    def setStartTime(self):
        START_TIME = self.startTime
        return str(START_TIME)

    def getChargeStatus(self):
        CHARGE = self.charge
        if CHARGE == False:
            return False

    def setChargeStatus(self, charge):
        if charge == 'Y':
            CHARGE == True
            return CHARGE

        #else:
            #return 'The car is charged'

    #def setDistanceRemain(self):


    #def getDistanceRemain(self):


    #def updateDistance(self):


    #def getElapsedTime(self):



#endregion



