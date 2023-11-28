from dataclasses import dataclass, field
from netex.beacon_point_version_structure import BeaconPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BeaconPoint(BeaconPointVersionStructure):
    """
    A POINT where a beacon or similar device to support the automatic detection of
    vehicles passing by is located.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
