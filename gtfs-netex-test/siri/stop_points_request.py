from dataclasses import dataclass

from .stop_points_discovery_request_structure import StopPointsDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopPointsRequest(StopPointsDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
