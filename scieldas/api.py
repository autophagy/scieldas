from typing import Any, List

import requests
from scieldas.deserializers import HTMLDeserializer, JSONDeserializer, XMLDeserializer


class BaseAPIException(Exception):
    def __init__(self, response: requests.Response):
        self.target = response.request.url
        self.code = response.status_code
        self.response = response.content

    def __repr__(self):
        return " // ".join(
            [f"{self.__class__.__name__}", f"Code :: {self.code}", f"{self.response}"]
        )


class HttpNotFoundException(BaseAPIException):
    pass


class HttpClientException(BaseAPIException):
    pass


class HttpServerException(BaseAPIException):
    pass


class API:
    """
    A thin wrapper around requests, in order to make API requests to various services.
    """

    deserializers = {
        "json": JSONDeserializer,
        "xml": XMLDeserializer,
        "html": HTMLDeserializer,
    }

    def __init__(self, base_url: str, deserializer="json", suffix=None):
        assert base_url is not None
        self.base_url = base_url
        self.resources: List[str] = []
        assert deserializer in self.deserializers
        self.deserializer = self.deserializers.get(deserializer, JSONDeserializer)()
        self.suffix = suffix

    def _create_url(self) -> str:
        res_path = "/".join(self.resources)
        suffix = self.suffix if self.suffix else ""
        return f"{self.base_url}{res_path}{suffix}"

    def add(self, *argv: str) -> "API":
        for arg in argv:
            self.resources.append(arg)
        return self

    def get(self, headers: dict = None, params: dict = None) -> Any:
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        headers.update({"accept": self.deserializer.get_content_type()})
        r = requests.get(self._create_url(), headers=headers, params=params)
        if 400 <= r.status_code <= 499:
            if r.status_code == 404:
                raise HttpNotFoundException(r)
            else:
                raise HttpClientException(r)
        elif 500 <= r.status_code <= 599:
            raise HttpServerException(r)

        content_type = r.headers.get("content-type", "")
        if content_type.split(";")[0] in self.deserializer.content_types:
            return self.deserializer.deserialize(r)
        else:
            try:
                return self.deserializer.deserialize(r)
            except Exception:
                return r.text
