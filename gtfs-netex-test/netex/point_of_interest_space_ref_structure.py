from dataclasses import dataclass
from netex.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestSpaceRefStructure(SiteComponentRefStructure):
    """
    Type for reference to a POINT OF INTEREST SPACE.
    """
