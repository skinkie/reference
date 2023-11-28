from dataclasses import dataclass, field
from netex.access_zone_version_structure import AccessZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessZone(AccessZoneVersionStructure):
    """An identified storey (ground, first, basement, mezzanine, etc) within an
    interchange building or SITE on which SITE COMPONENTs reside.

    A PATH LINK may connect components on different ACCESS ZONEs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
