from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .site_path_link import SitePathLink
from .site_path_link_ref import SitePathLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLinksRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathLinks_RelStructure"

    site_path_link_ref_or_site_path_link: List[Union[SitePathLinkRef, SitePathLink]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SitePathLinkRef",
                    "type": SitePathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
