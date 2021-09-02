from typing import TYPE_CHECKING

from pydantic import BaseModel


if TYPE_CHECKING:
    IPvAnyAddress = str
else:
    from pydantic import IPvAnyAddress


class Proxy(BaseModel):
    """Data model for proxy information."""

    anonymity: str
    country: str
    ip: IPvAnyAddress
    port: str
    proto: str
