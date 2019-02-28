from typing import Optional
from xml.dom.minidom import Document, Element

from scieldas.api import API
from scieldas.services import ServiceAPI


class Jetbrains(ServiceAPI):
    base_url = "https://plugins.jetbrains.com/plugins/"
    deserializer = "xml"

    @ServiceAPI.call
    def downloads(self, plugin_id: str, api: API) -> Optional[int]:
        details: Document = api.add("list").get(params={"pluginId": plugin_id})
        repo = details.getElementsByTagName("plugin-repository")[0]
        category = repo.getElementsByTagName("category")
        if len(category) == 0:
            return None
        plugin: Element = category[0].getElementsByTagName("idea-plugin")[0]
        return int(plugin.getAttribute("downloads"))

    @ServiceAPI.call
    def version(self, plugin_id: str, api: API) -> Optional[str]:
        details: Document = api.add("list").get(params={"pluginId": plugin_id})
        repo = details.getElementsByTagName("plugin-repository")[0]
        category = repo.getElementsByTagName("category")
        if len(category) == 0:
            return None
        plugin: Element = category[0].getElementsByTagName("idea-plugin")[0]
        return plugin.getElementsByTagName("version")[0].firstChild.nodeValue
