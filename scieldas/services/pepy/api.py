from typing import Optional
from xml.dom.minidom import Document
from xml.parsers.expat import ExpatError

from scieldas.api import API
from scieldas.services import ServiceAPI


class PePy(ServiceAPI):
    base_url = "https://pepy.tech/badge/"
    deserializer = "xml"

    @ServiceAPI.call
    def downloads(self, project: str, api: API) -> Optional[int]:
        try:
            doc: Document = api.add(project).get()
            if type(doc) != Document:
                return None
            return doc.getElementsByTagName("text")[-1].firstChild.nodeValue.upper()
        except ExpatError:
            return None
