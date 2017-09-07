# -*- coding: utf-8 -*-
from character import Character
from roll import Roll
import random


class Human(Character):
    def __init__(self):
        self.char_ancestry = "Human"
        self.char_strength = 10
        self.char_agility = 10
        self.char_intellect = 10
        self.char_will = 10
        attribute_to_increase = random.choice([
            "strength", "agility", "intelect", "will"])
        if attribute_to_increase == "strength":
            self.char_strength = 11
        elif attribute_to_increase == "agility":
            self.char_agility = 11
        elif attribute_to_increase == "intelect":
            self.char_intellect = 11
        elif attribute_to_increase == "will":
            self.char_will = 11
        self.char_health = self.char_strength
        self.char_healing_rate = round(self.char_health/4, 0)
        self.char_perception = self.char_intellect
        self.char_defense = self.char_agility
        self.char_size = "1/2 or 1"
        self.char_speed = 10
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "You speak the Common Tongue, and you can \
either speak one additional language or add a random profession."

    def generate_extra_info(self, char, print_extra_info):
        char.generate_info("build", Roll.a_dice("3d6"))
        char.generate_info("religion", Roll.a_dice("3d6"))
        char.generate_info("age", Roll.a_dice("3d6"))
        char.generate_info("appearence", Roll.a_dice("3d6"))
        if print_extra_info:
            print("Age: " + char.char_age)
            print("Appearence: " + char.char_appearence)
            print("Build: " + char.char_build)
            print("Religion: " + char.char_religion)
