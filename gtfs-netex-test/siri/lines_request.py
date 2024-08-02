from dataclasses import dataclass

from .lines_discovery_request_structure import LinesDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LinesRequest(LinesDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
