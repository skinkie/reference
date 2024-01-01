from dataclasses import dataclass
from .accommodation_ref_structure import AccommodationRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationRef(AccommodationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
