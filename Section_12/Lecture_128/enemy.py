import random


class Enemy(object):
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        self._points = self._hit_points

    def take_damage(self, damage):
        remaining_points = self._points - damage
        if remaining_points >= 0:
            self._points = remaining_points
            print("I took {0} points of damage and have {1} left".format(damage, self._points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0.name} lost a life.".format(self))
                self._points = self._hit_points
            else:
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit Points: {0._points}".format(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        assert isinstance(name, str)


class Troll(Enemy):
    def __init__(self, name):
        super(Troll, self).__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you.".format(self))


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("{0._name} dodges.".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140
        self._points=140

    def take_damage(self, damage):
        super().take_damage(int(damage / 4))
