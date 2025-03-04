from dataclasses import dataclass

from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReplacingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Replacing_VersionStructure"
