from dataclasses import dataclass

from .type_of_time_demand_type_structure import TypeOfTimeDemandTypeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfTimeDemandType(TypeOfTimeDemandTypeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
