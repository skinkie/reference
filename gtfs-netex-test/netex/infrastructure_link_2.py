from dataclasses import dataclass

from .link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfrastructureLink2(LinkVersionStructure):
    class Meta:
        name = "InfrastructureLink_"
        namespace = "http://www.netex.org.uk/netex"
