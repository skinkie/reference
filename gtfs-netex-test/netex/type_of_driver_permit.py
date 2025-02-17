from dataclasses import dataclass

from .type_of_driver_permit_value_structure import TypeOfDriverPermitValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfDriverPermit(TypeOfDriverPermitValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
