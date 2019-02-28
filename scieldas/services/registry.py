import logging
from types import ModuleType
from typing import Dict, List

from .service import Service

LOGGER = logging.getLogger(__name__)


class Registry:
    registered_categories: Dict[str, List[Service]] = {}
    category_documentation: Dict[str, str] = {}

    def init_app(self, application):
        self.application = application

    def register(self, category: str, service_module: ModuleType):
        assert category not in self.registered_categories
        services = []
        for name in dir(service_module):
            property = getattr(service_module, name)
            if type(property) == type and issubclass(property, Service):
                services.append(property(flask_instance=self.application))
        LOGGER.info(f"Registering {len(services)} service(s) for '{category}'")
        self.registered_categories[category] = sorted(services, key=lambda x: x.name)
        if hasattr(service_module, "DOCUMENTATION"):
            self.category_documentation[category] = getattr(
                service_module, "DOCUMENTATION"
            )

    @property
    def service_count(self):
        service_count = 0
        for services in list(self.registered_categories.values()):
            service_count += len(services)
        return service_count
