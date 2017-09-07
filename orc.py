# -*- coding: utf-8 -*-
from character import Character
from roll import Roll


class Orc(Character):
    def __init__(self):
        self.char_ancestry = "Orc"
        self.char_strength = 11
        self.char_agility = 10
        self.char_intellect = 9
        self.char_will = 9
        self.char_health = self.char_strength
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect + 1
        self.char_defense = self.char_agility
        self.char_size = "1"
        self.char_speed = 12
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 1
        self.char_languages = "You speak the Common Tongue and Elvish."

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("build", Roll.a_dice("3d6"))
        char.generate_info("age", Roll.a_dice("3d6"))
        char.generate_info("appearence", Roll.a_dice("3d6"))
        if print_extra_info:
            print("Age: " + char.char_age)
            print("Appearence: " + char.char_appearence)
            print("Build: " + char.char_build)
