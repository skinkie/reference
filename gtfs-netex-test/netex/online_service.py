from dataclasses import dataclass

from .online_service_version_structure import OnlineServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OnlineService(OnlineServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
