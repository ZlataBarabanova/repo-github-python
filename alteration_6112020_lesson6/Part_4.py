class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("{} is going ".format(self.name))

    def stop(self):
        print("{} is stop ".format(self.name))

    def turn(self, direction=""):
        print('{} is turning to {}!'.format(self.name, direction))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Ваша скорость превышена")

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Ваша скорость превышена")

class PoliceCar(Car):
    pass

w = WorkCar(60, "Red", "Kamaz", False)
w.go()
w.stop()
w.turn("right")
w.show_speed()

s = SportCar(160, "Red", "Nissan", False)
s.go()
s.stop()
s.turn("right")
s.show_speed()

p = PoliceCar(100, "Green", "Ford", True)
p.go()
p.stop()
p.turn("left")
p.show_speed()

t = TownCar(150, "Green", "Ford", True)
t.go()
t.stop()
t.turn("left")
t.show_speed()