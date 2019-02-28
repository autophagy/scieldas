from math import floor, log


class Shield:
    def create(self, content=None, params=None):
        raise NotImplementedError


class StateShield(Shield):
    def __init__(
        self, states, prefix=None, default_state="none", default_text="Unknown"
    ):
        self.prefix = prefix
        self.default = default_state
        self.states = states
        self.states[default_state] = default_text

    def create(self, content=None, params=None):
        if params is None:
            params = {}
        prefix = next(filter(None, [params.get("prefix"), self.prefix]), None)
        if prefix:
            return " :: ".join(
                [prefix, self.states.get(str(content).lower(), self.default)]
            )
        else:
            return self.states.get(content.lower(), self.default)


class TextShield(Shield):
    def __init__(self, prefix=None, suffix=None, default="Unknown"):
        self.prefix = prefix
        self.suffix = suffix
        self.default = default

    @staticmethod
    def _readable_number(number):
        if number == 0:
            return str(number)
        units = ["", "K", "M", "G", "T", "P"]
        magnitude = int(floor(log(abs(number), 1000)))
        amnt = round((abs(number) / 1000 ** magnitude), 2)
        if magnitude == 0 and isinstance(abs(number), int):
            amnt = int(amnt)
        sign = "-" if number < 0 else ""
        return f"{sign}{amnt}{units[magnitude]}"

    def create(self, content=None, params=None):
        if params is None:
            params = {}
        if isinstance(content, (int, float, complex)):
            content = TextShield._readable_number(content)
        t = self.default if content is None else content
        s = []

        prefix = next(filter(None, [params.get("prefix"), self.prefix]), None)
        suffix = next(filter(None, [params.get("suffix"), self.suffix]), None)

        if prefix:
            s.append(f"{prefix} :: ")
        s.append(t)
        if suffix:
            s.append(suffix)
        return "".join(s)


class RatingShield(Shield):
    def __init__(self, min=0, max=5, prefix=None, default="Unknown"):
        self.min = min
        self.max = max
        self.prefix = prefix
        self.default = default

    @staticmethod
    def _create_stars(rating: float, max: int) -> str:
        r = round(rating)
        return ("●" * r) + ("○" * (max - r))

    def create(self, content=None, params=None):
        if params is None:
            params = {}
        prefix = next(filter(None, [params.get("prefix"), self.prefix]), None)
        ratings = (
            RatingShield._create_stars(content, self.max)
            if content is not None
            else self.default
        )
        if prefix:
            return f"{self.prefix} :: {ratings}"
        else:
            return ratings
