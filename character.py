# -*- coding: utf-8 -*-
from info_generator import Generator as generate
import random


class Character(object):
    def __init__(
                self, char_name, char_ancestry, char_level, char_profession,
                char_age, char_appearence, char_background, char_personality,
                char_strength, char_intellect, char_agility, char_will,
                char_health, char_size, char_speed, char_power, char_damage,
                char_insanity, char_corruption, char_languages,
                char_interesting_thing, char_pos_personality_trait_a,
                char_pos_personality_trait_b, char_neg_personality_trait):
        self.char_name = char_name
        self.char_ancestry = char_ancestry
        self.char_level = char_level
        self.char_profession = char_profession
        self.char_age = char_age
        self.char_appearence = char_appearence
        self.char_background = char_background
        self.char_strength = char_strength
        self.char_intellect = char_intellect
        self.char_agility = char_intellect
        self.char_will = char_will
        self.char_health = char_health
        self.char_personality = char_personality
        self.char_size = char_size
        self.char_speed = char_speed
        self.char_power = char_power
        self.char_damage = char_damage
        self.char_insanity = char_insanity
        self.char_corruption = char_corruption
        self.char_languages = char_languages
        self.char_interesting_thing = char_interesting_thing
        self.char_pos_personality_trait_a = char_pos_personality_trait_a
        self.char_pos_personality_trait_b - char_pos_personality_trait_b
        self.char_neg_personality_trait = char_neg_personality_trait

    def generate_name(self):
        info = "names"
        names = generate.ancestry_info(self.char_ancestry, info)[info]
        self.char_name = names[random.randint(0, len(names) - 1)]

    def generate_info(self, info, roll):
        attribute_name = "self.char_" + info
        exec(attribute_name + """ = generate.ancestry_info(
            self.char_ancestry, info)[roll]""")