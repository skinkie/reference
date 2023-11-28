from dataclasses import dataclass
from netex.version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionRef(VersionRefStructure):
    """
    Reference to a VERSION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
