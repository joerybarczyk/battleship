"""Contains all Axis objects"""


class Axis:
    """Base class for representing grid axis"""

    def __init__(self, start: int, end: int):
        """
        Constructs necessary attributes for axis object

        Attributes
        ----------
        start : int
            axis starting point
        end : int
            axis ending point
        """
        self.numbers = range(start, end)
        self.markers = [str(_) for _ in self.numbers]

    def __str__(self):
        return " ".join(self.markers)

    def __getitem__(self, index):
        return self.markers[index]


class NumAxis(Axis):
    """Axis with numerical markers, spaced to fit grid"""

    def __str__(self):
        """Reduce space between double-digit numbers to preserve even spacing throughout"""
        numaxis_str = "  "
        for num in self.numbers:
            if num < 10:
                numaxis_str += f"   {num}"
            else:
                numaxis_str += f"  {num}"
        return numaxis_str


class CharAxis(Axis):
    """Axis with alphabetic markers"""

    def __init__(self, start, end):
        super().__init__(start, end)
        self.markers = [chr(_ + 65) for _ in self.numbers]
