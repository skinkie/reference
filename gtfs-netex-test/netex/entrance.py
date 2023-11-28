from dataclasses import dataclass
from netex.site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Entrance(SiteEntranceVersionStructure):
    """A physical entrance or exit to/from a SITE.

    Maybe a door, barrier, gate or other recognizable point of access.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
