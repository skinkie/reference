from dataclasses import dataclass, field
from typing import List
from netex.link_on_section import LinkOnSection
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinksOnSectionRelStructure(StrictContainmentAggregationStructure):
    """Type for a list of LINKS on SECTION.

    +v1.1.
    """
    class Meta:
        name = "linksOnSection_RelStructure"

    link_on_section: List[LinkOnSection] = field(
        default_factory=list,
        metadata={
            "name": "LinkOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
