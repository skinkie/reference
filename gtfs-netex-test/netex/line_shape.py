from dataclasses import dataclass, field
from netex.line_shape_structure_2 import LineShapeStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineShape(LineShapeStructure2):
    """
    The graphical shape of a LINK obtained from a formula or other means, using the
    LOCATION of its limiting POINTs and depending on the LOCATING SYSTEM used for
    the graphical representation.

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
