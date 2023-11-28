from dataclasses import dataclass, field
from netex.general_zone_version_structure import GeneralZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeneralZone(GeneralZoneVersionStructure):
    """
    A GENERAL ZONE used to define a zonal fare structure in a zone-counting or
    zone-matrix system.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
