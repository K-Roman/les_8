class Robot:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class CanFly:

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity)


class Drone(Robot, CanFly):

    def __init__(self, model):
        Robot.__init__(self, model)
        CanFly.__init__(self)


    def operate(self):
        print('Робот ведет разведку с воздуха')

    def __str__(self):
        return 'model {}'.format(self.model) + ' высота {} скорость {}'.format(self.altitude, self.velocity)


orbiter = Drone(model='Orbiter II')
print(orbiter)
orbiter.take_off()
print(orbiter)
orbiter.fly()
print(orbiter.altitude)
print(orbiter)
orbiter.operate()
print(orbiter)
orbiter.land_on()
print(orbiter)
print(orbiter.altitude)
