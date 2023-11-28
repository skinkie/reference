from dataclasses import dataclass, field
from netex.navigation_path_version_structure import NavigationPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPath(NavigationPathVersionStructure):
    """A designated path between two places.

    May include an ordered sequence of PATH LINKs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
