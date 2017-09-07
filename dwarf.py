# -*- coding: utf-8 -*-
from character import Character
from roll import Roll


class Dwarf(Character):
    def __init__(self):
        self.char_ancestry = "Dwarf"
        self.char_strength = 10
        self.char_agility = 9
        self.char_intellect = 10
        self.char_will = 10
        self.char_health = self.char_strength + 4
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect + 1
        self.char_defense = self.char_agility
        self.char_size = "1/2"
        self.char_speed = 8
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "You speak the Common Tongue, and you speak, \
read, and write Dwarfish."

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("build", Roll.a_dice("3d6"))
        char.generate_info("hatred", Roll.a_dice("1d20"))
        char.generate_info("age", Roll.a_dice("3d6"))
        char.generate_info("appearence", Roll.a_dice("3d6"))
        if print_extra_info:
            print("Age: " + char.char_age)
            print("Appearence: " + char.char_appearence)
            print("Build: " + char.char_build)
            print("Hatred: " + char.char_hatred)
