from dataclasses import dataclass, field
from typing import List
from netex.accommodation import Accommodation
from netex.accommodation_ref import AccommodationRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationsRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE FACILITY SETs.
    """
    class Meta:
        name = "accommodations_RelStructure"

    accommodation_ref_or_accommodation: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccommodationRef",
                    "type": AccommodationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Accommodation",
                    "type": Accommodation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
