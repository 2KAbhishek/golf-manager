import datetime
from golfer import Golfer

class PCHolder(Golfer):
    def __init__(self, name, membership):
        super().__init__(name, membership)
        self._expiryDate = None

    def getMembershipStatus(self):
        if self._expiryDate == None:
            return True
        else:
            return self._expiryDate > datetime.datetime.now()

    def renew(self, expiryDate):
        self._expiryDate = expiryDate

    def getHandicap(self):
        return 99.9

    def __str__(self):
        return super().__str__() + " Expiry: {}".format(self._expiryDate)
