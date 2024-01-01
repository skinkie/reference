from dataclasses import dataclass
from .type_of_zone_ref_structure import TypeOfZoneRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfZoneRef(TypeOfZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
