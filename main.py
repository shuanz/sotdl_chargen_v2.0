# -*- coding: utf-8 -*-
from human import Human
from changeling import Changeling
from clockwork import Clockwork
from dwarf import Dwarf
from goblin import Goblin
from orc import Orc
from roll import Roll
from printer import Printer
import random

character = random.choice(
    [Human(), Changeling(), Clockwork(), Dwarf(), Goblin(), Orc()])
character.generate_name()
character.char_level = 0
character.generate_info("background", Roll.a_dice("1d20"))
character.generate_info("personality", Roll.a_dice("3d6"))
character.generate_profession(Roll.a_dice("1d20"))
character.generate_personality(
    Roll.a_dice("1d20"), Roll.a_dice("1d20"), Roll.a_dice("1d20"))
character.generate_interesting_things(Roll.a_dice("1d6"), Roll.a_dice("1d20"))
character.generate_wealth(Roll.a_dice("3d6"))
Printer.print_common_info(character)
character.generate_extra_info(character, True)

# to-dos
# add seed database generator
# add pdf cheet generator
# add descriptions
