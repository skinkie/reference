from dataclasses import dataclass, field
from netex.rounding_versioned_structure import RoundingVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Rounding(RoundingVersionedStructure):
    """
    Parameters describing how the results of calculations are to be rounded to the
    nearest quantum.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
