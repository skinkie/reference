from dataclasses import dataclass

from .connection_links_delivery_structure import ConnectionLinksDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinksDelivery(ConnectionLinksDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
