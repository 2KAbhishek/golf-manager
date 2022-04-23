'''
Implement the Hole class, which models a single hole on a golf course.
 Instance variables:
o _number: an integer number from 1 to 18, indicating the order of play.
o _par: PAR indicates the number of strokes a golfer is expected to complete
playing of the hole.
o _distance: representing the length of the hole in meters, from tee box to the
pin/cup.
o _index: an integer number from 1 to 18, representing the difficulty ranking
of the hole in a golf course, with a lower number signifying a more difficult
hole.
 Method getDuration computes the estimated time to complete playing the hole.
The formula to compute the duration is “Setup time + Play time”, in seconds, as
illustrated below in Figure 2
'''


from switch import Switch


class Hole:
    def __init__(self, number, par, distance, index):
        self._number = number
        self._par = par
        self._distance = distance
        self._index = index

    def getDuration(self):
        getSetupTime = Switch({
            range(1, 7): self._par * 180,
            range(7, 13): self._par * 150,
            range(13, 19): self._par * 120
        })

        getPlayTime = Switch({
            range(1, 101): 60,
            range(101, 201): 120,
            range(201, 301): 180,
            range(301, 401): 240,
            range(401, 501): 300,
            range(501, 9999): 360,
        })

        setupTime = getSetupTime(self._index)
        playTime = getPlayTime(self._distance)

        return setupTime + playTime

    def getNumber(self):
        return self._number

    def getPar(self):
        return self._par

    def getDistance(self):
        return self._distance

    def getIndex(self):
        return self._index
