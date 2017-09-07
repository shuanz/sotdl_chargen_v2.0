# -*- coding: utf-8 -*-
from character import Character
from human import Human
from dwarf import Dwarf
from goblin import Goblin
from orc import Orc
from roll import Roll


class Changeling(Character):
    def __init__(self):
        self.char_ancestry = "Changeling"
        self.char_strength = 9
        self.char_agility = 10
        self.char_intellect = 10
        self.char_will = 10
        self.char_health = self.char_strength
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect + 1
        self.char_defense = self.char_agility
        self.char_size = "1"
        self.char_speed = 10
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "You speak Common Tongue"

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("apparent_ancestry", Roll.a_dice("3d6"))
        char.generate_info("apparent_gender", Roll.a_dice("1d6"))
        char.generate_info("true_age", Roll.a_dice("3d6"))
        char.generate_info("quirk", Roll.a_dice("1d20"))
        print("Apparent Ancestry: " + char.char_apparent_ancestry)
        print("Apparent Gender: " + char.char_apparent_gender)
        print("True Age: " + char.char_true_age)
        print("Quirk: " + char.char_quirk)
        if "human" in char.char_apparent_ancestry:
            apparent_Ancestry = Human()
        elif "dwarf" in char.char_apparent_ancestry:
            apparent_Ancestry = Dwarf()
        elif "goblin" in char.char_apparent_ancestry:
            apparent_Ancestry = Goblin()
        elif "orc" in char.char_apparent_ancestry:
            apparent_Ancestry = Orc()
        apparent_Ancestry.generate_extra_info(apparent_Ancestry, False)
        print("Apparent Age: " + apparent_Ancestry.char_age)
        print("Apparent Build: " + apparent_Ancestry.char_build)
        print("Apparent Appearence: " + apparent_Ancestry.char_appearence)
