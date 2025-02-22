from dataclasses import dataclass

from .type_of_mobility_service_value_structure import TypeOfMobilityServiceValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfMobilityService(TypeOfMobilityServiceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
