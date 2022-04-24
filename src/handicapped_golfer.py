from golfer import Golfer

class HandicappedGolfer(Golfer):
    def __init__(self, name, membership, handicap):
        super().__init__(name, membership)
        self._handicap = handicap

    def getHandicap(self):
        return self._handicap

    def __str__(self):
        return super().__str__() + " Handicap: {}".format(self._handicap)
