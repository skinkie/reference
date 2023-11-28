from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_section_ref import FareSectionRef
from netex.section_in_sequence_versioned_child_structure import FareSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareSectionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE SECTIONs.
    """
    class Meta:
        name = "fareSections_RelStructure"

    fare_section_ref_or_fare_section: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareSectionRef",
                    "type": FareSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareSection",
                    "type": FareSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
