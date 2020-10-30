from random import randrange
from items import*
from list import*


def full_display_player(player):
    print("""
{}
Life: {}
Stamina: {}
Armor: {}
Strenght: {}
Gold: {}
""".format(player.name, player.life, player.stamina, player.armor, player.strenght, player.gold))


def min_display_player(player):
    print("""You:
    Life: {} // Stamina: {}""".format(player.life, player.stamina))


def full_display_monster(mob):
    print("""{}
Life: {}
Armor: {}
Strenght: {}
        """.format(mob.name, mob.life, mob.armor, mob.strenght))


def min_display_monster(mob):
    print("""{}:
    Life: {}""".format(mob.name, mob.life))


def display_menu(ab1, ab2, ab3):
    print("""
(1): {}
(2): {}
(3): {}
(4): Inventory
""".format(ab1.name, ab2.name, ab3.name))


def display_inventory():
    var = 0


def use_ability(player, monster, ability):
    if ability.damage > 0:
        monster.damaged(player.strenght + ability.damage - monster.armor)
        print("You dealt {} damages, after deducting {} armor".format((player.strenght+ability.damage-monster.armor), monster.armor))
    if ability.heal > 0:
        player.life += ability.heal
        print("you have regained  ", ability.heal, " life points.")
    player.stamina -= ability.cost_stamina


def ennemy_turn(player, monster):
    print("Ennemy turn !")
    player.damaged(monster.strenght - player.armor)
    print("{} dealt {} damages, after deducting {} armor".format(monster.name, (monster.strenght-player.armor), player.armor))


def passive_stamina(player):
    player.stamina += randrange(3, 22, 1)
    if player.stamina < 0:
        player.stamina = 0
    if player.stamina > 100:
        player.stamina = 100


def player_action(player, monster, ab1, ab2, ab3):
    in_player = input("Chose your action ?")
    in_player = int(in_player)
    if in_player == 1:
        if player.stamina < ab1.cost_stamina:
            print("Not enought energy !")
            player_action(player, monster, ab1, ab2, ab3)
        use_ability(player, monster, ab1)
    elif in_player == 2:
        if player.stamina < ab2.cost_stamina:
            print("Not enought energy !")
            player_action(player, monster, ab1, ab2, ab3)
        use_ability(player, monster, ab2)
    elif in_player == 3:
        if player.stamina < ab3.cost_stamina:
            print("Not enought energy !")
            player_action(player, monster, ab1, ab2, ab3)
        use_ability(player, monster, ab3)
    elif in_player == 4:
        display_inventory()
    else:
        print("Error")
        player_action(player, monster, ab1, ab2, ab3)


def shop(player):
    val = 0
    print("Gold avaible {}".format(player.gold))
    for i in range(3, 11):
        obj = Item(*all_item[i])
        print("({}) {}, avaible for {}".format(i, obj.name, obj.price))
    print("(11) Exit")
    val = input("Need Something ?")
    val = int(val)
    if val > 12 or val < 3:
        print("Error")
        return 0
    if val == 11:
        return 0
    else:
        return val


def ask_id(ab1, ab2, ab3):
    val = input("""
Which item did you want to replace ? 
(1) {}
(2) {}
(3) {}
""".format(ab1.name, ab2.name, ab3.name))
    val = int(val)
    if val < 1 or val > 4:
        print("Error!")
        ask_id(ab1, ab2, ab3)
    if val == 1:
        return 1
    elif val == 2:
        return 2
    else:
        return 3


def new_turn(player, monster, ab1, ab2, ab3):
    print("----- New Turn -----")
    min_display_player(player)
    min_display_monster(monster)
    display_menu(ab1, ab2, ab3)
    player_action(player, monster, ab1, ab2, ab3)
    ennemy_turn(player, monster)


