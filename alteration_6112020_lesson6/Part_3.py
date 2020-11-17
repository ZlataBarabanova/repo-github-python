class Worker():

    def __init__(self, name, surname, position):
        self._income = {'Wage': 100000, 'bonus': 0.2}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return (self.name + ' ' + self.surname)

    def get_total_income(self):
        return self._income['Wage'] + \
               self._income['Wage'] * self._income['bonus']

p = Position("Иван", "Иванов", "Programmer")
print(p.get_full_name())
print(p.get_total_income())