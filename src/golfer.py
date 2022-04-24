class Golfer:
    _NEXT_ID = 1

    def __init__(self, name, membership):
        self._memberID = Golfer._NEXT_ID
        self._name = name
        self._membership = membership
        self._status = True
        Golfer._NEXT_ID += 1

    @property
    def memberID(self):
        return self._memberID

    @property
    def name(self):
        return self._name

    @property
    def membership(self):
        return self._membership

    @membership.setter
    def membership(self, membership):
        self._membership = membership

    def getMembershipStatus(self):
        return self._status

    def setMembershipStatus(self, status):
        self._status = status

    def getHandicap(self):
        pass

    def __str__(self):
        return "Member ID: {}\t Name: {}\t Membership: {}".format(self._memberID, self._name, self._membership)
