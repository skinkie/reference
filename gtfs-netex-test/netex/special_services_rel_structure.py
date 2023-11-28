from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.dated_special_service_ref import DatedSpecialServiceRef
from netex.special_service import SpecialService
from netex.special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpecialServicesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SPECIAL SERVICE s.
    """
    class Meta:
        name = "specialServices_RelStructure"

    dated_special_service_ref_or_special_service_ref_or_special_service: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
