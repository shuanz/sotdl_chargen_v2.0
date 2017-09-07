# -*- coding: utf-8 -*-


class Printer():
    @classmethod
    def print_common_info(self, character):
        print("Name: " + character.char_name)
        print("Level: " + str(character.char_level))
        print("Ancestry: " + character.char_ancestry)
        print("Character Size: " + character.char_size)
        print("Languages: " + character.char_languages)
        print("Background: " + character.char_background)
        print("Personality: " + character.char_personality)
        print("Profession: " + character.char_profession)
        print(
            "Attributes: " + "Strength:" + str(character.char_strength),
            "Agility:" + str(character.char_agility) + " Intelect:" +
            str(character.char_intellect) + " Will:" + str(character.char_will)
            + " Health:" + str(character.char_health) + " Speed:" +
            str(character.char_speed) + " Power:" + str(character.char_power) +
            " Damage:" + str(character.char_damage) + " Insanity:" +
            str(character.char_insanity) + " Corruption:" +
            str(character.char_corruption))
        print(
            "Positives Personality Traits: " +
            character.char_pos_personality_trait_a + " & " +
            character.char_pos_personality_trait_b)
        print(
            "Negative Personality Trait: " +
            character.char_neg_personality_trait)
        print("Interesting Thing: " + character.char_interesting_things)
        print("Wealth: " + character.char_wealth)
