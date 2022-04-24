import datetime
from golfing_exception import GolfingException
from pc_holder import PCHolder
from handicapped_golfer import HandicappedGolfer


class Flight:
    def __init__(self, golfers):
        if len(golfers) < 3 or len(golfers) > 4:
            raise GolfingException(
                "Flight can only consists of 3 or 4 golfers")
        for golfer in golfers:
            if golfer.getMembershipStatus() == False:
                raise GolfingException("Golfer {} {} has inactive membership"
                                       .format(golfer.memberID, golfer.name))
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


if __name__ == "__main__":
    golfers1 = [
        HandicappedGolfer("Jeff", "Full", 13.1),
        HandicappedGolfer("Jim", "Basic", 4),
        HandicappedGolfer("Joe", "Full", 19),
        HandicappedGolfer("Jack", "Full", 2.3),
    ]
    flight1 = Flight(golfers1)
    basicGolfer = flight1.searchGolfer(2)
    basicGolfer.membership = "Full"
    print("Flight1 Weekend eligibility {}".format(flight1.getWeekendEligibility()))

    golfers2 = [
        HandicappedGolfer("Tom", "Full", 11),
        HandicappedGolfer("Neil", "Full", 2.5),
        PCHolder("Charles", "Full", datetime.datetime(2021, 7, 31))
    ]
    try:
        flight2 = Flight(golfers2)
    except GolfingException as e:
        renewedGolfer = golfers2[2]
        renewedGolfer.renew(datetime.datetime(2032, 7, 31))
        flight2 = Flight(golfers2)
    print("Flight2 Weekend eligibility {}".format(flight2.getWeekendEligibility()))
