class Monster:

    def __init__(self, new_name, new_life, new_armor, new_strenght, new_gold_value):
        self.name = new_name
        self.life = new_life
        self.armor = new_armor
        self.strenght = new_strenght
        self.gold_value = new_gold_value

    def damaged(self, damage):
        self.life -= damage
