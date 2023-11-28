from dataclasses import dataclass, field
from netex.notice_version_structure import NoticeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Notice(NoticeVersionStructure):
    """A note or footnote about any aspect of a service, e.g. an announcement,
    notice, etc.

    May have different DELIVERY VARIANTs for different media.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
