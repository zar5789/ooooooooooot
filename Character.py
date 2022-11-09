from weapons import *

class Character():
    def __init__(self):
        self.health = 100
        self.weapon = PunchBehavior()

    def attack(self):
        return self.weapon.use_weapon()

    def take_damage(self, damage):
        self.health = self.health - damage
        
    def set_weapon(self, weapon):
        if isinstance(weapon, WeaponBehavior):
            self.weapon = weapon
            print(f'equip {self.weapon.name}')

    def self_destruction(self):
        self.health = 1
        return self.weapon.use_weapon() * 10

class Knight(Character):
    def attack(self):
        return self.weapon.use_weapon() * 10.0

class King(Character):
    def take_damage(self, damage):
        self. health = self.health - 0.2 * damage

class Dickman(Character):
    def __init__(self):
        super().__init__()
        self.health = 1
        self.weapon = DickBehavior()

class Troll(Character):
    def __init__(self):
        super().__init__()
        self.weapon = KnifeBehavior()

class Ghost(Character):
    def __init__(self):
        super().__init__()
        self.health = 300

    def attack(self):
        count = 0
        if count > 3:
            return self_destruction()

    def take_damage(self, damage):
        self.health = self.health - 0.5 * damage