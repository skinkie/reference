from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .off_site_path_link import OffSitePathLink
from .path_link import PathLink
from .site_path_link import SitePathLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "sitePathLinksInFrame_RelStructure"

    site_path_link_or_off_site_path_link_or_path_link: List[Union[SitePathLink, OffSitePathLink, PathLink]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SitePathLink",
                    "type": SitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OffSitePathLink",
                    "type": OffSitePathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLink",
                    "type": PathLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
