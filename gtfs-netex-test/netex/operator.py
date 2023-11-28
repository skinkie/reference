from dataclasses import dataclass, field
from netex.operator_version_structure import OperatorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Operator(OperatorVersionStructure):
    """
    A company  providing public transport services.

    :ivar id: Identifier of  OPERATOR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
