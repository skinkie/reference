from dataclasses import dataclass
from netex.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReplacingVersionStructure(ResellingVersionStructure):
    """
    Type for REPLACING.
    """
    class Meta:
        name = "Replacing_VersionStructure"
