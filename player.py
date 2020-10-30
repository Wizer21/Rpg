class Player:

    def __init__(self, new_name, new_life, new_stamina, new_armor, new_strenght):
        self.name = new_name
        self.life = new_life
        self.stamina = new_stamina
        self.armor = new_armor
        self.strenght = new_strenght
        self.gold = 0

    def damaged(self, damage):
        self.life -= damage
