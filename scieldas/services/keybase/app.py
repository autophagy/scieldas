from scieldas.services import Service
from scieldas.shields import TextShield

from .api import Keybase

api = Keybase()


class PGP(Service):
    name = "Keybase PGP Key"
    shield = TextShield(prefix="PGP")
    base = "keybase"
    example = "48A4E913F7236FBA"
    routes = ["pgp/:username"]

    def route(self, username):
        fingerprint = api.pgp(username)
        if fingerprint is not None:
            return fingerprint[-16:].upper()
        return fingerprint
