"""
posix:
export FLASK_APP=index.py
windows:
set FLASK_APP=index.py
flask run
"""
from flask import Flask, render_template
from human import Human
from changeling import Changeling
from clockwork import Clockwork
from dwarf import Dwarf
from goblin import Goblin
from orc import Orc
from roll import Roll
from printer import Printer
import random
app = Flask(__name__)


@app.route("/")
def create_char():
    character = random.choice(
        [Human(), Changeling(), Clockwork(), Dwarf(), Goblin(), Orc()])
    character.generate_name()
    character.char_level = 0
    character.generate_info("background", Roll.a_dice("1d20"))
    character.generate_info("personality", Roll.a_dice("3d6"))
    character.generate_profession(Roll.a_dice("1d20"))
    character.generate_personality(
        Roll.a_dice("1d20"), Roll.a_dice("1d20"), Roll.a_dice("1d20"))
    character.generate_interesting_things(
        Roll.a_dice("1d6"), Roll.a_dice("1d20"))
    character.generate_wealth(Roll.a_dice("3d6"))
    Printer.print_common_info(character)
    character.generate_extra_info(character, True)
    return render_template('index.html', character=character)
