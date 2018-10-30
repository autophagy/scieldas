class StateButton(object):
    def __init__(
        self, states, prefix=None, default_state="unknown", default_text="Unknown"
    ):
        self.prefix = prefix
        self.default = default_state
        self.states = states
        self.states[default_state] = default_text

    def create(self, state=""):
        if self.prefix:
            return f"{self.prefix} :: {self.states.get(state, self.default)}"
        else:
            return self.states.get(state, self.default)


class TextButton(object):
    def __init__(self, prefix=None, default="Unknown"):
        self.prefix = prefix
        self.default = default

    def create(self, text=""):
        t = text if len(text) > 0 else self.default
        if self.prefix:
            return f"{self.prefix} :: {t}"
        else:
            return t
