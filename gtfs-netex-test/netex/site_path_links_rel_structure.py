from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.path_link_ref import PathLinkRef
from netex.site_path_link import SitePathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SitePathLinksRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of SITE PATH LINKs.
    """
    class Meta:
        name = "sitePathLinks_RelStructure"

    path_link_ref_or_site_path_link: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
