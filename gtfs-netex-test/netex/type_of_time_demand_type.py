from dataclasses import dataclass, field
from netex.type_of_time_demand_type_structure import TypeOfTimeDemandTypeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTimeDemandType(TypeOfTimeDemandTypeStructure):
    """
    Classification of a TIME DEMAND TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
