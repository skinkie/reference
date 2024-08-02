from dataclasses import dataclass

from .connection_links_discovery_request_structure import ConnectionLinksDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionLinksRequest(ConnectionLinksDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
