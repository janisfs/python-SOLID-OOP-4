from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает {type(new_weapon).__name__}")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")
        else:
            print(f"{self.name} без оружия")


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")


# Пример использования классов
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч
sword = Sword()
fighter.change_weapon(sword)
fighter.attack()
monster.defeat()

# Боец выбирает лук
bow = Bow()
fighter.change_weapon(bow)
fighter.attack()
monster.defeat()
