from dataclasses import dataclass, field

from .info_link import InfoLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InfoLinksRelStructure:
    class Meta:
        name = "infoLinks_RelStructure"

    info_link: list[InfoLink] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
