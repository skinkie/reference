from dataclasses import dataclass

from .mobility_service_version_structure import MobilityServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MobilityService1(MobilityServiceVersionStructure):
    class Meta:
        name = "MobilityService"
        namespace = "http://www.netex.org.uk/netex"
