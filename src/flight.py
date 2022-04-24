from golfing_exception import GolfingException

class Flight:
    def __init__(self, golfers):
        if len(golfers) < 3 or len(golfers) > 4:
            raise GolfingException("Flight can only consists of 3 or 4 golfers")
        for golfer in golfers:
            if golfer.membership != "Full" or golfer.getMembershipStatus() == False:
                raise GolfingException(golfer.name + " has inactive membership")
        self._golfers = golfers

    def searchGolfer(self, memberID):
        for golfer in self._golfers:
            if golfer.memberID == memberID:
                return golfer
        return None

    def getGolfersID(self):
        return [golfer.memberID for golfer in self._golfers]

    def getWeekendEligibility(self):
        for golfer in self._golfers:
            if golfer.membership != "Full" or golfer.getMembershipStatus() == False:
                return False
        return True
