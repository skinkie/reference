from dataclasses import dataclass
from netex.link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureLinkVersionStructure(LinkVersionStructure):
    """
    Type for INFRASTRUCTURE LINK.
    """
    class Meta:
        name = "InfrastructureLink_VersionStructure"
