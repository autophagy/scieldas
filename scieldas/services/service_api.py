import logging
from typing import Optional

from requests import exceptions
from scieldas.api import (
    API,
    HttpClientException,
    HttpNotFoundException,
    HttpServerException,
)

LOGGER = logging.getLogger(__name__)


class ServiceAPI:
    base_url: str
    deserializer: str = "json"
    suffix: Optional[str] = None

    def __init__(self):
        assert self.base_url is not None

    @staticmethod
    def call(func):
        """
        Wraps an API response call in standard error handling.
        """

        def wrapper(*args, **kwargs):
            try:
                api = API(
                    base_url=args[0].base_url,
                    deserializer=args[0].deserializer,
                    suffix=args[0].suffix,
                )
                return func(*args, **kwargs, api=api)
            except HttpNotFoundException:
                return None
            except (HttpClientException, HttpServerException) as e:
                LOGGER.error(f"Unexpected Error: Target {e.target}")
                LOGGER.error(f"Code: {e.code}")
                LOGGER.error(f"Response: {e.response}")
                return None
            except exceptions.RequestException as e:
                LOGGER.error(f"Unexpected Requests Error!")
                LOGGER.error(str(e))
                return None
            except AssertionError:
                return None

        return wrapper

    @staticmethod
    def api_response(func):
        """
        Wraps an API response call in standard error handling.
        """

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except HttpNotFoundException:
                return None
            except (HttpClientException, HttpServerException) as e:
                LOGGER.error(f"Unexpected Error: Target {e.target}")
                LOGGER.error(f"Code: {e.code}")
                LOGGER.error(f"Response: {e.response}")
                return None

        return wrapper
