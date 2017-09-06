from human import Human
from roll import Roll


character = Human(None, None)
character.generate_name()
character.generate_info("age", Roll.a_dice("3d6"))
character.generate_info("build", Roll.a_dice("3d6"))
character.generate_info("appearence", Roll.a_dice("3d6"))
character.generate_info("background", Roll.a_dice("1d20"))
character.generate_info("personality", Roll.a_dice("3d6"))
character.generate_info("religion", Roll.a_dice("3d6"))
character.generate_profession(Roll.a_dice("1d20"))
print(character.char_name)
print(character.char_ancestry)
print(character.char_age)
print(character.char_build)
print(character.char_appearence)
print(character.char_background)
print(character.char_personality)
print(character.char_religion)
print(character.char_profession)
