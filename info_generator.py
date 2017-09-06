# -*- coding: utf-8 -*-
from load_json import Import
import os


character_file = Import()
ancestry_path = ".%sancestries%s%s%s%s_%s.json"
profession_path = ".%sprofessions%s%s.json"


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
