import datetime
from hole import Hole


class Course:
    def __init__(self, filename):
        self._name = filename.split(".")[0]
        self._holes = []
        self._totalPar = 0
        self._readFile(filename)

    def _readFile(self, filename):
        """Read the file and create the holes"""
        with open(filename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if line:
                    par, index, distance = line.split(',')
                    self._totalPar += int(par)
                    self._holes.append(
                        Hole(i, int(par), int(distance), int(index)))

    @property
    def name(self):
        return self._name

    def getPlaySchedule(self, teeTime):
        """Get the play schedule for the course"""
        print("Tee Off Time: {}".format(teeTime))
        print("Course: {} \t\t Total PAR: {}".format(self._name, self._totalPar))
        print("Hole\t PAR\t Index\t Distance\t Start\t Finish")
        for i, hole in enumerate(self._holes):
            print("{}\t {}\t {}\t {}\t {}\t {}".format(i+1, hole.getPar(), hole.getIndex(),
                  hole.getDistance(), teeTime, teeTime + datetime.timedelta(seconds=hole.getDuration())))

    def __str__(self):
        """String representation of the course"""
        out = "Course: {} \t\t Total PAR: {}\n".format(
            self._name, self._totalPar)
        out += "Hole\t PAR\t Index\t Distance\n"
        for i, hole in enumerate(self._holes):
            out += "{}\t {}\t {}\t {}\n".format(
                i+1, hole.getPar(), hole.getIndex(), hole.getDistance())
        return out
