import re
from collections import namedtuple
from functools import wraps
from typing import Dict, List, Optional, Union

from flask import Flask, abort, make_response
from scieldas.descriptor import Descriptor
from scieldas.image_creator import create_image
from scieldas.shields import Shield


class Service:
    """
    A base class that facilitates creation of service routes based on the base,
    routes and route function.
    Should never be called directly, only implemented as a base class.
    """

    name: str
    example: Optional[Union[str, int, float]] = None
    shield: Shield
    base: str
    routes: List[str]
    bounded_params: Dict[str, Dict[str, List[str]]]

    Response = namedtuple("Response", "content params")

    def __init__(self, flask_instance: Flask):
        if self.base is None or len(self.routes) == 0:
            raise NotImplementedError()

        for idx, r in enumerate(self.routes):
            route, bounded_params = self.flaskify_route(r)
            route = f"/{self.base}/{route}.<filetype>"
            self.bounded_params = bounded_params
            flask_instance.add_url_rule(
                route,
                f"{self.__module__}.{self.__class__}[{idx}].route",
                self.image_response(self.dispatch),
            )

    @staticmethod
    def image_response(func):
        """
        Creates either an svg or a png image.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                shield, filetype = func(*args, **kwargs)
                image = create_image(shield, filetype)
                if filetype == "svg":
                    response = make_response(image.tostring())
                    response.content_type = "image/svg+xml"
                else:
                    response = make_response(image)
                    response.content_type = "image/png"
                response.cache_control.max_age = 60
                return response
            except ValueError:
                abort(404)

        return wrapper

    def example_routes(self):
        """
        Returns the list of routes, for documentation/index purposes.
        """
        return list(map(lambda r: f"{self.base}/{r}.svg", self.routes))

    @staticmethod
    def flaskify_route(route):
        """
        Returns a flask valid route for a service.
        There are 3 valid components of a route:

        static (/component/) - this just adds a static part of the route.
        param (/:param/) - This section of a route corresponds to a flask
                           parameter
        bounded (/:bounded(a|b|c)/ - Like a param, but can only be of values
                                     defined between '|' characters.
        """
        elements = route.split("/")
        flask_elements = []
        bounded_params = {}
        variable_pattern = re.compile(r"^:(\w+)(?:\(((?:\w+\|{0,1})+)\)){0,1}$")
        for element in elements:
            match = variable_pattern.match(element)
            if match:
                flask_elements.append(f"<{match.group(1)}>")
                if match.group(2):
                    bounded_params[match.group(1)] = match.group(2).split("|")
            else:
                flask_elements.append(element)
        return "/".join(flask_elements), bounded_params

    def get_descriptor(self):
        return Descriptor(
            self.name, self.example_routes(), self.shield, example=self.example
        )

    def dispatch(self, *args, **kwargs):
        filetype = kwargs.pop("filetype", "svg")

        try:
            for param, binds in self.bounded_params.items():
                if kwargs.get(param):
                    assert kwargs.get(param) in binds
        except AssertionError:
            return self.shield.create(content="Unknown"), filetype

        result = self.route(*args, **kwargs)
        if isinstance(result, self.Response):
            return (
                self.shield.create(content=result.content, params=result.params),
                filetype,
            )
        else:
            return self.shield.create(content=result), filetype

    def route(self, *args, **kwargs):
        raise NotImplementedError()
