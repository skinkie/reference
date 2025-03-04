from dataclasses import dataclass, field

from .link_on_section import LinkOnSection
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinksOnSectionRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "linksOnSection_RelStructure"

    link_on_section: list[LinkOnSection] = field(
        default_factory=list,
        metadata={
            "name": "LinkOnSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
