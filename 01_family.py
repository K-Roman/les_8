# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    coats = 0
    many = 0
    food = 0

    def __init__(self):
        self.many = 100
        self.food = 100
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return "В доме осталось еды - {}, денег - {}, грязно примерно на {},  и еды для кота осталось {}"\
            .format(self.food, self.many, self.dirt, self.cat_food)


class Husband:

    def __init__(self, name, house, cat):
        self.name = name
        self.happiness = 100
        self.satiety = 30
        self.house = house
        self.cat = cat

    def __str__(self):
        return "{} сытый на {}, счастлив на {}".format(self.name, self.satiety, self.happiness)

    def act(self):
        if self.satiety <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.satiety < 21 and self.house.food >=41:
            self.eat()
        elif self.house.many < 70:
            self.work()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.gaming()
        if self.house.dirt > 90:
            self.happiness -= 10
            cprint('{} немного расстроился от грязи вокруг'.format(self.name), color='red')

    def eat(self):
        if self.house.food >= 41:
            vol = randint(10, 30)
            self.satiety += vol
            self.house.food -= vol
            House.food += vol
            cprint('{} поел'.format(self.name), color='cyan')
        else:
            cprint('{} не покушал'.format(self.name), color='red')
            self.satiety -= 10

    def work(self):
        self.satiety -= 10
        self.house.many += 150
        House.many += 150
        cprint('{} поработал'.format(self.name), color='cyan')

    def gaming(self):
        self.satiety -= 10
        self.happiness += 20
        cprint('{} рубился в танки'.format(self.name), color='cyan')


class Wife:

    def __init__(self, name, house, cat):
        self.name = name
        self.happiness = 100
        self.satiety = 30
        self.house = house
        self.cat = cat

    def __str__(self):
        return "{} сытая на {}, счастлива на {}".format(self.name, self.satiety, self.happiness)

    def act(self):
        if self.satiety <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            return
        if self.happiness < 10:
            cprint('{} умерла от депрессии'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.satiety <= 21 and self.house.food >= 41:
            self.eat()
        elif self.house.food < 41 or self.house.cat_food <= 12:
            self.shopping()
        elif self.house.dirt > 100:
            self.clean_house()
        elif self.house.many > 400:
            self.buy_fur_coat()
        elif dice == 1:
            cprint('{} вышивала весь день'.format(self.name), color='red')
            self.satiety -= 10
        elif dice == 2:
            cprint('{} гладила кота {}'.format(self.name, self.cat.name), color='red')
            self.happiness += 5

        if self.house.dirt > 90:
            self.happiness -= 10
            cprint('{} немного расстроилась от грязи вокруг'.format(self.name), color='red')
        self.house.dirt += 5


# dice = randint(1, 2)
# if dice == 1:
# self.eat()
# elif dice == 2:
# self.shopping()
# self.house.dirt += 5


    def eat(self):
        if self.house.food >= 41:
            vol = randint(10, 30)
            self.satiety += vol
            self.house.food -= vol
            House.food += vol
            cprint('{} покушала'.format(self.name), color='yellow')
        else:
            cprint('{} не покушала'.format(self.name), color='yellow')
            self.satiety -= 10

    def shopping(self):
        self.satiety -= 10
        self.house.many -= 50
        self.house.food += 50
        cprint('{} закупилась продуктами'.format(self.name), color='yellow')
        if self.house.cat_food <= 12:
            self.house.cat_food += 20
            self.house.many -= 20
            cprint('{} закупилась продуктами для кота'.format(self.name), color='yellow')

    def buy_fur_coat(self):
        self.satiety -= 10
        self.house.many -= 350
        self.happiness += 60
        House.coats += 1
        cprint('{} наконец-то купила шубу и счастлива'.format(self.name), color='yellow')

    def clean_house(self):
        self.satiety -= 10
        self.house.dirt -= 100
        cprint('{} прибралась'.format(self.name), color='yellow')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.house = house

    def __str__(self):
        return "Кот {} сытый на {}".format(self.name, self.satiety)

    def act(self):
        if self.satiety < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.satiety < 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.soil()

    def eat(self):
        if self.house.cat_food > 10:
            n = randint(1, 10)
            self.house.cat_food -= n
            self.satiety += 2*n
            cprint('{} поел'.format(self.name), color='green')
        else:
            cprint('{} не поел'.format(self.name), color='red')

    def sleep(self):
        self.satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='green')

    def soil(self):
        self.satiety -= 10
        self.house.dirt += 5
        cprint('{} подрал сука обои'.format(self.name), color='green')


home = House()
cat = Cat("Мурзик", house=home)
serge = Husband(name='Сережа',house=home, cat=cat)
masha = Wife(name='Маша', house=home, cat=cat)


for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='green')
    cprint(cat, color='yellow')
print(House.food, "единиц")
print(House.many, "руб")
print(House.coats, "шт")



######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов





######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

