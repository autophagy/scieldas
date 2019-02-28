from scieldas.services import Service
from scieldas.shields import StateShield


class Licenses(Service):
    name = "Licenses"
    example = "150k"
    shield = StateShield({"mit": "MIT", "apache": "Apache 2", "gpl": "GPL 3"})
    base = "misc"
    routes = ["licenses/:license(mit|apache|gpl)"]

    def route(self, license):
        return license


class CodeStyles(Service):
    name = "Code Styles"
    example = "150k"
    shield = StateShield(
        {"black": "Black", "yapf": "Yapf", "autopep8": "AutoPEP8"}, prefix="Style"
    )
    base = "misc"
    routes = ["styles/:style(black|yapf|autopep8)"]

    def route(self, style):
        return style
