from dataclasses import dataclass, field
from netex.cell_versioned_child_structure import TimeStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeStructureFactor(TimeStructureFactorVersionStructure):
    """
    The value of a TIME INTERVAL or a DISTANCE MATRIX ELEMENT expressed by a TIME
    UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
