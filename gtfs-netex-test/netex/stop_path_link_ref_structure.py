from dataclasses import dataclass
from .path_link_ref_structure import PathLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPathLinkRefStructure(PathLinkRefStructure):
    value: RestrictedVar
