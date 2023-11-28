from dataclasses import dataclass, field
from netex.route_instruction_version_structure import RouteInstructionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteInstruction(RouteInstructionVersionStructure):
    """
    An Instruction on how to follow a ROUTE through the network.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
