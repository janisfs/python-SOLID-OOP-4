from abc import ABC, abstractmethod


# Абстрактный базовый класс для оружия
class Weapon:
    @abstractmethod
    def use(self, target):
        pass


# Конкретные реализации оружия
class Sword(Weapon):
    def use(self, target):
        print(f"Вы используете меч против {target}")


class Bow(Weapon):
    def use(self, target):
        print(f"Вы используете лук против {target}")


# Класс игрока
class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, target):
        self.weapon.use(target)


# Класс Монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name} атакует {target}")


# Применение
sword = Sword()
player = Player("Вася", sword)
monster = Monster("Монстр")
player.attack("Монстр")
bow = Bow()
player = Player("Вася", bow)
player.attack("Монстр")