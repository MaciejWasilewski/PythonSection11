# lectures 128,129, 130, 131, 132, 133, 134, 135, 136, 137
from Lecture_128.player import Player

tim = Player("Tim")

from Lecture_128.enemy import Troll, Vampyre, VampyreKing

troll = Troll('ug')
print(troll)
print(troll.grunt())
print(troll._name)

v1=Vampyre('Lestat')

vk=VampyreKing("Maciej")
print(vk)
vk.take_damage(100)