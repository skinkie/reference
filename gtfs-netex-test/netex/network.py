from dataclasses import dataclass

from .network_version_structure import NetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Network(NetworkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
