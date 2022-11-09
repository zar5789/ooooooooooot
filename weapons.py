class WeaponBehavior():
    def use_weapon(self):
        raise NotImplementError

class PunchBehavior(WeaponBehavior):
    def __init__(self):
        self.name = 'punch'

    def use_weapon(self):
        print('punching')
        return 10

class SwordBehavior(WeaponBehavior):
    def __init__(self):
        self.name = 'sword'

    def use_weapon(self):
        print('slash')
        return 100

class KnifeBehavior(WeaponBehavior):
    def __init__(self):
        self.name = 'knife'

    def use_weapon(self):
        print('stab')
        return 40

class AxeBehavior(WeaponBehavior):
    def __init__(self):
        self.name = 'Axe'

    def use_weapon(self):
        print('heavy slash')
        return 130

class DickBehavior(WeaponBehavior):
    def __init__(self):
        self.name = 'This is a dick'

    def use_weapon(self):
        print('fuck')
        return 9999999999999999