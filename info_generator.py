# -*- coding: utf-8 -*-
from load_json import Import
import os
import random


character_file = Import()
ancestry_path = ".%sancestries%s%s%s%s_%s.json"
profession_path = ".%sprofessions%s%s.json"
profession_type = random.choice([
    "academic", "common", "criminal", "martial", "religious", "wilderness"])
personality_path = ".%spersonality_traits%s%s_personality_traits.json"


class Generator():
    @classmethod
    def ancestry_info(self, char_ancestry, char_info):
        if os.name == "posix":
            attributes_list = character_file.json_file(ancestry_path % (
                "/", "/", char_ancestry, "/", char_ancestry, char_info))
        else:
            attributes_list = character_file.json_file(ancestry_path % (
                "\\", "\\", char_ancestry, "\\", char_ancestry, char_info))
        return(attributes_list)

    @classmethod
    def profession_info(self):
        if os.name == "posix":
            profession_list = character_file.json_file(profession_path % (
                "/", "/", profession_type))
        else:
            profession_list = character_file.json_file(profession_path % (
                "\\", "\\", profession_type))
        return(profession_list)

    @classmethod
    def personality_info(self, personality_type):
        if os.name == "posix":
            personality_list = character_file.json_file(personality_path % (
                "/", "/", personality_type))
        else:
            personality_list = character_file.json_file(personality_path % (
                "\\", "\\", personality_type))
        return(personality_list)
