from Character import *
from weapons import *
import random
from space_weapon import *


class Environment():
    def __init__(self, hero):
        self.hero = hero
        self.current_enemy = Troll()
        self.kill_count = 0

    def step(self, action):
        if action == 'attack':
            damage_from_enemy = self.current_enemy.attack()
            self.hero.take_damage(damage_from_enemy)

            damage = self.hero.attack()
            self.current_enemy.take_damage(damage)

        elif action == 'defend':
            damage_from_enemy = self.current_enemy.attack()
            self.hero.take_damage(0.1 * damage_from_enemy)

        elif action == 'destruction':
            damage = self.hero.self_destruction()
            self.current_enemy.take_damage(damage)

        if self.current_enemy.health <= 0:
            print('enemy has been slain')
            self.kill_count += 1
            self.current_enemy = random.choice([Troll(), Ghost()])
            return random.choice([SwordBehavior(), AxeBehavior()])

        else:
            return None


if __name__ == "__main__":

    my_hero = Knight()

    env = Environment(my_hero)

    for i in range(100):
        drop = env.step('attack')
    print(f'Hero kills {env.kill_count} enemies.')