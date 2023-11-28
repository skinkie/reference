from dataclasses import dataclass, field
from netex.geographical_unit_version_structure import GeographicalUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnit(GeographicalUnitVersionStructure):
    """
    A factor influencing access rights definition or calculation of prices.

    :ivar id: Identifier of a GEOGRAPHICAL UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
