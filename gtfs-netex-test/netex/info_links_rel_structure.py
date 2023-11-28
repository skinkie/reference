from dataclasses import dataclass, field
from typing import List
from netex.info_link import InfoLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfoLinksRelStructure:
    """
    Type for collection of info links.
    """
    class Meta:
        name = "infoLinks_RelStructure"

    info_link: List[InfoLink] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
