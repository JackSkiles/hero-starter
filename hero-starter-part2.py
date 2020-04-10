"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self, name='<undefined>', health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.is_alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if not self.is_alive():
            print("Oh no! %s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    # def __init__(self, name, health):
    #     super().__init__(name)
    #     super().__init__(health)    
    
    def double_attack(self, target):
        attack1 = 1
        while attack1 <= 1:
            random_number = random.randint(0, 4)
            if random_number == 1:
                self.power = 10
            else:
                self.power = 5
            super().attack(target)
            attack1 += 1
            
        

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)







class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 10, 2, 0)






class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 8, 1, 0)

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super().attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power


class Medic(Character):
    def heal(self):
        random_heal = random.randint(0, 4)
        if random_heal == 1:
            self.health += 2
            print(f'{chopper.name} has healed 2 damage')
    def heal_friend(self, target):
        target.health += 5
        print(f'{self.name} has healed {hero.name} by 5 points!')

    def raise_dead(self, target):
        if target == evil_dead:
            target.health = 0
            print(f'{self.name} Cast raise on {target.name}! {target.name} has become one of the living again.')
        else:
            print(f'raise does nothing on already living beings.')



class Shadow(Character):
    def dodge_attack(self):
        dodge = random.randint(0, 10)
        if dodge != 1:
            self.health = 1
            print(f'{self.name} doged the attack')


class Zombie(Character):
    def immortality(self):
        if self.health <= 0:
            self.health = 5
            print('you cannot kill a zombie')
        


class Battle:
    def do_battle(self, hero, enemy):
        print("=====================")
        print("%s faces the %s" % (hero.name, enemy.name))
        print("=====================")
        while hero.is_alive() and enemy.is_alive() and chopper.is_alive():
            hero.print_status()
            enemy.print_status()
            chopper.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. Chopper healing")
            print("3. flee")
            print("4. run away")
            print("> ",)
            user_input = int(input())

            if enemy == evil_dead:
                user_input2 = int(input())
                print("you are facing evil dead. What would you like to do?")
                print("1. Attack Enemy")
                print("2 Cast raise on enemy")
                if user_input2 == 1:
                    hero.double_attack(enemy)
                    evil_dead.immortality()
                elif user_input2 == 2:
                    chopper.raise_dead(evil_dead)
            if user_input == 1:
                hero.double_attack(enemy)
                if enemy == shadow:
                   shadow.dodge_attack()
            
            elif user_input == 2:
                chopper.heal_friend(hero)
            elif user_input == 3:
                pass
            elif user_input == 4:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
            enemy.attack(chopper)
            chopper.heal()

        if hero.is_alive():
            print("You defeated the %s" % enemy.name)
            return True
        else:
            print("YOU LOSE!")
            return False






class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))







class Sword:
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))






class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)





hero = Hero('Oakley', 50)
chopper = Medic('Chopper', 30, 5)
shadow = Shadow('Shadow', 1, 10)
evil_dead = Zombie('Evil Dead', 5, 5)
enemies = [Goblin('Bob'), Wizard('Jethro'), evil_dead, shadow]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
