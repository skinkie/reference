from dataclasses import dataclass, field
from netex.responsibility_set_version_structure import ResponsibilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilitySet(ResponsibilitySetVersionStructure):
    """A set of responsibility roles assignments that can be associated with a DATA
    MANAGED OBJECT.

    A Child ENTITY has the same responsibilities as its parent.

    :ivar id: Identifier of RESPONSIBILITY SET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
