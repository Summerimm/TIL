
class Creature:
    def __init__(self):
        self.hp = 0
        self.attack = 0
        self.defense = 0

    def attack_target(self, target):
        print(f"{self} attack {target}")
        damage = self.attack - target.defense
        target.hp -= damage if self.attack > target.defense else 1
        if target.hp <= 0:
            print(f"Oh, {target} is down! I repeat. {target} is down!")
        else:
            print(f"{target}'s hp: {target.hp}")


class Hero(Creature):
    def __init__(self):
        super().__init__()
        self.hp = 150
        self.attack = 10
        self.defense = 10

    def __str__(self):
        return "Hero"

    def set_magic_power(self):
        # set the Hero Status(hp, attack, defense)
        self.hp = 150
        self.attack = 600
        self.defense = 40

class Dragon(Creature):
    def __init__(self):
        super().__init__()
        self.hp = 1000
        self.attack = 50
        self.defense = 100

    def __str__(self):
        return "Dragon"


hero = Hero()
hero.set_magic_power()
dragon = Dragon()
while (hero.hp > 0) and (dragon.hp > 0):
    hero.attack_target(dragon)
    if dragon.hp > 0:
        dragon.attack_target(hero)
