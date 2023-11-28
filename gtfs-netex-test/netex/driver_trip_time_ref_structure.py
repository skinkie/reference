from dataclasses import dataclass
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverTripTimeRefStructure(VersionOfObjectRefStructure):
    """
    Type for Reference to a DRIVER TRIP TIME.
    """
