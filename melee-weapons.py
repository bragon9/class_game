from random import randint

class MeleeWeapon:
    ''' Parent class for all melee weapons.
        Weapons should have the following attributes:
        self.damage_range = damage_range
            Tuple of low and high damage ex: (1, 5), (3, 100)
        self.damage_type = damage_type
            String, ex: 'Sharp', 'Blunt'
        self.elemental_damage = elemental_damage
            List of type and damage ranges in tuple, ex: [('Frost', (1, 5)), ('Fire', (2, 6))]
        self.attack_speed = attack_speed
            Attack speed ex: 1.3, 2.6
        self.size = size
            How many hands to wield ex: 1, 2
        self.attack_range = attack_range
            Range ex: 1, 4'''
    def __init__(self, name):
        self.name = name
        self.elemental_damage = []

    def __str__(self):
        return self.name

    def attack(self):
        ''' Return a random number between the low and high of the weapon'''
        damage = [(self.damage_type, randint(self.damage_range[0], self.damage_range[1]))]
        for i in self.elemental_damage:
            ele_damage_type = i[0]
            ele_damage = randint(i[1][0], i[1][1])
            damage.append((ele_damage_type, ele_damage))
        return damage

    def sharpen(self, increase_amount):
        '''Increase the weapon damage by an amount'''
        self.damage_range = (self.damage_range[0] + increase_amount, self.damage_range[1] + increase_amount)

    def enchant(self, damage_type, damage_range):
        '''Add/increase elemental damage on a weapon'''
        pass

class Sword(MeleeWeapon):
    '''Parent class for all swords.'''
    def __init__(self, name):
        MeleeWeapon.__init__(self, name)
        self.damage_type = 'Sharp'

class ShortSword(Sword):
    '''Short Sword'''
    def __init__(self, name):
        Sword.__init__(self, name)
        self.damage_range = (2, 5)
        self.attack_speed = 1.5
        self.size = 1
        self.attack_range = 2

class Dagger(MeleeWeapon):
    '''Parent class for all daggers.'''
    def __init__(self, name):
        MeleeWeapon.__init__(self, name)
        self.damage_type = 'Sharp'

class PocketKnife(Dagger):
    '''Pocket Knife'''
    def __init__(self, name):
        Dagger.__init__(self, name)
        self.damage_range = (1, 2)
        self.attack_speed = 2.5
        self.size = 1
        self.attack_range = 1
