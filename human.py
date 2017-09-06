# -*- coding: utf-8 -*-
from character import Character


class Human(Character):
    def __init__(self, build, religion):
        self.build = build
        self.religion = religion
        self.char_ancestry = "Human"
        self.char_strength = 10
        self.char_agility = 10
        self.char_intellect = 10
        self.char_will = 10
        self.char_size = "1/2 or 1"
        self.char_speed = self.char_agility
        self.char_power = 0
        self.char_damage = 0
        self.char_insanity = 0
        self.char_corruption = 0
        self.char_languages = "Common Tongue"
