from dataclasses import dataclass
from netex.type_of_time_demand_type_ref_structure import TypeOfTimeDemandTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTimeDemandTypeRef(TypeOfTimeDemandTypeRefStructure):
    """
    Reference to a TYPE OF TIME DEMAND TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
