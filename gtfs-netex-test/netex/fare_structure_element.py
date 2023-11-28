from dataclasses import dataclass, field
from netex.fare_structure_element_version_structure import FareStructureElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElement(FareStructureElementVersionStructure):
    """
    A sequence or set of CONTROLLABLE ELEMENTs to which rules for limitation of
    access rights and calculation of prices (fare structure) are applied.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
