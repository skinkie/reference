from dataclasses import dataclass
from .taxi_service_place_assignment_ref_structure import (
    TaxiServicePlaceAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiServicePlaceAssignmentRef(TaxiServicePlaceAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
