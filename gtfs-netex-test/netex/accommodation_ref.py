from dataclasses import dataclass

from .accommodation_ref_structure import AccommodationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccommodationRef(AccommodationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
