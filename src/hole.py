from switch import Switch

class Hole:
    def __init__(self, number, par, distance, index):
        self._number = number
        self._par = par
        self._distance = distance
        self._index = index

    def getDuration(self):
        """Get duration of the hole playtime in seconds
        Returns:
            int: duration of the hole playtime in seconds
        """
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

        setupTime = getSetupTime[self._index]
        playTime = getPlayTime[self._distance]

        return setupTime + playTime

    def __str__(self):
        """String representation of the hole"""
        return "{}\t{}\t{}\t{}".format(self._number, self._par, self._index, self._distance)
