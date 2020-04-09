"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from lib.hero import Hero
from lib.goblin import Goblin

cloud = Hero(100, 30, 'Cloud')
goblin = Goblin(40, 10)


def main():
    # hero_health = cloud.health
    # hero_power = cloud.power
    # goblin_health = goblin.health
    # goblin_power = goblin.power

    while cloud.is_alive(cloud) and goblin.is_alive(goblin):
        print(cloud.print_status(cloud))
        print(goblin.print_status(goblin))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            cloud.attack(cloud, goblin)
            print(f'{cloud.name} does %d damage to the goblin.' % cloud.power)
            if goblin.is_alive(goblin) == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(goblin, cloud)
            print("The goblin does %d damage to you." % goblin.power)
            if cloud.is_alive(cloud) == False:
                #cloud.increase_health(cloud)
                print("You are dead.")

main()
