class Road():
    _length = 0
    _width = 0

    def __init__(self, length=0, width=0):
        self._length=length
        self._width=width

    def calc(self):
        print(self._length * self._width * 25 * 0.05)

r = Road(20, 5000)
r.calc()
