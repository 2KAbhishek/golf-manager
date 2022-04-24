import datetime

from golfing_exception import GolfingException
from handicapped_golfer import HandicappedGolfer
from pc_holder import PCHolder


class GolfClub:
    _TEE_SLOTS = ["07:08", "07:18", "07:28", "07:38", "07:48", "07:58"]

    def __init__(self, name, course, golfingDate):
        self._name = name
        self._course = course
        self._golfers = {}
        self._bookings = {}
        self._golfingDate = golfingDate
        for teeTime in GolfClub._TEE_SLOTS:
            self._bookings[teeTime] = None

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

    @property
    def golfingDate(self):
        return self._golfingDate

    def setupGolfers(self, filename):
        with open(filename, "r") as f:
            for index, line in enumerate(f):
                line = line.strip()
                if line == "":
                    continue
                data = line.split(",")
                if "PC" in data:
                    self._golfers[index+1] = PCHolder(data[0], data[1],
                                                      datetime.datetime.strptime(data[3], "%d-%b-%Y"))
                else:
                    self._golfers[index +
                                  1] = HandicappedGolfer(data[0], data[1], data[2])

    def searchGolfer(self, memberID):
        if memberID in self._golfers:
            return self._golfers[memberID]
        else:
            return None

    def searchBooking(self, teeTime):
        if teeTime in self._bookings:
            return self._bookings[teeTime]
        else:
            return None

    def searchMemberBooking(self, memberID):
        for teeTime, flight in self._bookings.items():
            if flight != None and memberID in flight.getGolfersID():
                return teeTime
        return None

    def addBooking(self, teeTime, flight):
        if teeTime not in self._bookings:
            raise GolfingException("There is no such tee time")
        if self._bookings[teeTime] != None:
            raise GolfingException("Tee time is already booked")
        for golfer in flight.getGolfersID():
            if self.searchMemberBooking(golfer) != None:
                raise GolfingException(
                    "Booking has failed as one member already has another booking")
        if self._golfingDate.weekday() == 5 or self._golfingDate.weekday() == 6:
            if not flight.getWeekendEligibility():
                raise GolfingException(
                    "Booking has failed as flight is not eligible to play on weekend")
        self._bookings[teeTime] = flight

    def cancelBooking(self, teeTime):
        if teeTime not in self._bookings:
            raise GolfingException("There is no such tee time")
        if self._bookings[teeTime] == None:
            raise GolfingException("Tee time has no booking")
        self._bookings[teeTime] = None

    def getBookings(self):
        result = ""
        for teeTime in GolfClub._TEE_SLOTS:
            flight = self._bookings[teeTime]
            if flight == None:
                result += teeTime + " - no booking\n"
            else:
                result += teeTime + " - " + str(flight.getGolfersID()) + "\n"
        return result

    def getEmptyTeeTimes(self):
        result = []
        for teeTime in GolfClub._TEE_SLOTS:
            if self._bookings[teeTime] == None:
                result.append(teeTime)
        return result
