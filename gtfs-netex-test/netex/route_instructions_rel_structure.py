from dataclasses import dataclass, field
from typing import List
from netex.route_instruction_version_structure import RouteInstructionVersionStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteInstructionsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of ROUTE INSTRUCTIONs.

    :ivar route_instruction: A POINT used to define the shape of a ROUTE
        through the network.
    """
    class Meta:
        name = "routeInstructions_RelStructure"

    route_instruction: List["RouteInstructionsRelStructure.RouteInstruction"] = field(
        default_factory=list,
        metadata={
            "name": "RouteInstruction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class RouteInstruction(RouteInstructionVersionStructure):
        id: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
