# -*- coding: utf-8 -*-
from character import Character
from roll import Roll


class Clockwork(Character):
    def __init__(self):
        self.char_ancestry = "Clockwork"
        self.char_strength = 9
        self.char_agility = 8
        self.char_intellect = 9
        self.char_will = 9
        self.char_health = self.char_strength
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect
        self.char_defense = 13
        self.char_size = "1"
        self.char_speed = 8
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "You speak Common Tongue"

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("form", Roll.a_dice("3d6"))
        char.generate_info("appearence", Roll.a_dice("3d6"))
        char.generate_info("purpose", Roll.a_dice("1d20"))
        char.generate_info("age", Roll.a_dice("3d6"))
        if print_extra_info:
            print("Form: " + char.char_form)
            print("Appearence: " + char.char_appearence)
            print("Purpose: " + char.char_purpose)
            print("Age: " + char.char_age)
