from dataclasses import dataclass, field
from netex.network_version_structure import NetworkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Network(NetworkVersionStructure):
    """
    A named grouping of LINEs under which a Transport network is known.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
