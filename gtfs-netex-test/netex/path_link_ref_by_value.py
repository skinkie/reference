from dataclasses import dataclass
from .path_link_ref_by_value_structure import PathLinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkRefByValue(PathLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
