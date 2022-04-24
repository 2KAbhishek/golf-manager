class HandicappedGolfer(Golfer):
    def __init__(self, name, membership):
        super().__init__(name, membership)
        self._handicap = 0

    def getHandicap(self):
        return self._handicap

    def __str__(self):
        return str(super(HandicappedGolfer, self)) + " Handicap: {}".format(self._handicap)
