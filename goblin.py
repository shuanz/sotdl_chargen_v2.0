# -*- coding: utf-8 -*-
from character import Character
from roll import Roll


class Goblin(Character):
    def __init__(self):
        self.char_ancestry = "Goblin"
        self.char_strength = 8
        self.char_agility = 12
        self.char_intellect = 10
        self.char_will = 9
        self.char_health = self.char_strength
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect + 1
        self.char_defense = self.char_agility
        self.char_size = "1/2"
        self.char_speed = 10
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "You speak the Common Tongue and Elvish."

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("build", Roll.a_dice("3d6"))
        char.generate_info("odd_habit", Roll.a_dice("1d20"))
        char.generate_info("age", Roll.a_dice("3d6"))
        char.generate_info("appearence", Roll.a_dice("1d20"))
        if print_extra_info:
            print("Age: " + char.char_age)
            print("Distinctive Appearence: " + char.char_appearence)
            print("Build: " + char.char_build)
            print("Odd Habit: " + char.char_odd_habit)
