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
interesting_things_path = ".%sinteresting_things%stable_%s.json"
wealth_path = ".%swealth%swealth.json"


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

    @classmethod
    def interesting_things_info(self, roll):
        if os.name == "posix":
            interesting_things_list = character_file.json_file(
                interesting_things_path % ("/", "/", roll))
        else:
            interesting_things_list = character_file.json_file(
                interesting_things_path % ("\\", "\\", roll))
        return(interesting_things_list)

    @classmethod
    def wealth_info(self):
        if os.name == "posix":
            wealth_list = character_file.json_file(
                wealth_path % ("/", "/"))
        else:
            wealth_list = character_file.json_file(
                wealth_path % ("\\", "\\"))
        return(wealth_list)
