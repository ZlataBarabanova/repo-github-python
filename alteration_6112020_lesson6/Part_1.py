import time


class TrafficLight():
    __color = ''

    def running(self):
        self.__color = 'Red'
        print(self.__color)
        time.sleep(7)
        self.__color = 'Yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'Green'
        print(self.__color)
        time.sleep(7)


tr = TrafficLight()
tr.running()