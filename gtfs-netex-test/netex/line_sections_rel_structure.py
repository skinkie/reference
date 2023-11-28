from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.line_section_ref import LineSectionRef
from netex.section_in_sequence_versioned_child_structure import LineSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LineSectionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LINE SECTIONs.
    """
    class Meta:
        name = "lineSections_RelStructure"

    line_section_ref_or_line_section: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LineSectionRef",
                    "type": LineSectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineSection",
                    "type": LineSection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
