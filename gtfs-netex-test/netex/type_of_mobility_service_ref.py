from dataclasses import dataclass

from .type_of_mobility_service_ref_structure import TypeOfMobilityServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfMobilityServiceRef(TypeOfMobilityServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
