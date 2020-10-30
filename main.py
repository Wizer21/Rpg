from fonctions import*
from player import*
from monsters import*
from list import*
from items import*

killed_monsters = 1

print("Welcome to your last trip.")
name = input("Enter your name : ")
name = str(name)

hero = Player(name, 500, 100, 5, 20)
actual_monster = Monster(*all_monster[killed_monsters])
full_display_player(hero)
full_display_monster(actual_monster)

ability1 = Item(*all_item[2])
ability2 = Item(*all_item[1])
ability3 = Item(*all_item[1])

while hero.life > 0:
    passive_stamina(hero)
    new_turn(hero, actual_monster, ability1, ability2, ability3)
    if actual_monster.life <= 0:
        killed_monsters += 1
        hero.gold += actual_monster.gold_value
        print("""
{} passed away..
He dropped {} golds.
You now own {}.
        """.format(actual_monster.name, actual_monster.gold_value, hero.gold))
        actual_monster = Monster(*all_monster[killed_monsters])
        full_display_monster(actual_monster)
        new_item_id = 0
        new_item_id = shop(hero)
        if new_item_id != 0:
            temp_ability = Item(*all_item[new_item_id])
            if temp_ability.price <= hero.gold:
                hero.gold -= temp_ability.price
                if ability2.name == "None":
                    ability2 = temp_ability
                elif ability3.name == "None":
                    ability3 = temp_ability
                else:
                    id_chose = ask_id(ability1, ability2, ability3)
                    if id_chose == 1:
                        ability1 = temp_ability
                    elif id_chose == 2:
                        ability2 = temp_ability
                    else:
                        ability3 = temp_ability
            else:
                print("Not Enought gold")
