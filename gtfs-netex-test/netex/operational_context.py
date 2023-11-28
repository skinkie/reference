from dataclasses import dataclass, field
from netex.operational_context_version_structure import OperationalContextVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperationalContext(OperationalContextVersionStructure):
    """
    Characterization of a set of operational objects, such as timing or links
    determined either by a DEPARTMENT or by an ORGANISATIONAL UNIT.

    :ivar id: Identifier of  OPERATIONAL CONTEXT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
