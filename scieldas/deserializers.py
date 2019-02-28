from typing import List
from xml.dom import minidom

from bs4 import BeautifulSoup
from requests import Response


class Deserializer:

    content_types: List[str]

    def get_content_type(self):
        if len(self.content_types) == 0:
            raise NotImplementedError()
        else:
            return self.content_types[0]

    def deserialize(self, response: Response):
        raise NotImplementedError()


class JSONDeserializer(Deserializer):

    content_types = [
        "application/json",
        "application/x-javascript",
        "text/javascript",
        "text/x-javascript",
        "text/x-json",
    ]

    def deserialize(self, response: Response) -> dict:
        return response.json()


class XMLDeserializer(Deserializer):

    content_types = ["application/xml", "text/xml", "image/svg+xml"]

    def deserialize(self, response: Response) -> minidom.Document:
        return minidom.parseString(response.content)


class HTMLDeserializer(Deserializer):

    content_types = ["text/html"]

    def deserialize(self, response: Response) -> BeautifulSoup:
        return BeautifulSoup(response.content, "html.parser")
