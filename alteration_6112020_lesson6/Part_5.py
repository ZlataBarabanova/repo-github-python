class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print('{} is drawing'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('{} is drawing'.format(self.title))


class Marker(Stationery):
    def draw(self):
        print('{} is drawing'.format(self.title))


p = Pencil("Карандаш")
p.draw()
r = Pen("Ручка")
r.draw()
m = Marker("Маркер")
m.draw()