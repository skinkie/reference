from dataclasses import dataclass
from .reselling_version_structure import ResellingVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReplacingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Replacing_VersionStructure"
