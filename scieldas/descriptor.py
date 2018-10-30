from .button import StateButton
from . import image_creator
from flask import render_template


class Descriptor(object):
    def __init__(self, name, path, button, description=None, example=None):
        self.name = name
        self.path = path
        self.button = button
        self.description = description
        self.example = example

    def has_states(self):
        return isinstance(self.button, StateButton)

    def render(self, key):
        buttons = {}
        if self.has_states():
            for state in self.button.states:
                buttons[state] = image_creator.create_image(
                    "svg", self.button.create, state
                )
        else:
            buttons["example"] = image_creator.create_image(
                "svg", self.button.create, self.example
            )
        return render_template(
            "descriptor.html", descriptor=self, buttons=buttons, key=key
        )
