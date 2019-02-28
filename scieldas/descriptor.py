from flask import render_template
from scieldas import image_creator
from scieldas.shields import StateShield


class Descriptor:
    def __init__(self, name, paths, shield, example=None):
        self.name = name
        self.paths = paths
        self.shield = shield
        self.example = example

    def has_states(self):
        return isinstance(self.shield, StateShield)

    def render(self):
        buttons = {}
        if self.has_states():
            for state in self.shield.states:
                buttons[state] = image_creator.create_image(
                    self.shield.create(state), "svg"
                )
        else:
            buttons["example"] = image_creator.create_image(
                self.shield.create(self.example), "svg"
            )
        return render_template("descriptor.html", descriptor=self, buttons=buttons)
