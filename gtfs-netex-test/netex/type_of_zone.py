from dataclasses import dataclass

from .type_of_zone_value_structure import TypeOfZoneValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfZone(TypeOfZoneValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
