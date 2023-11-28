from dataclasses import dataclass, field
from netex.site_connection_version_structure import SiteConnectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteConnection(SiteConnectionVersionStructure):
    """
    The physical (spatial) possibility to connect from one point to another in a
    SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
