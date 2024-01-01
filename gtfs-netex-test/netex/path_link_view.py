from dataclasses import dataclass
from .path_link_derived_view_structure import PathLinkDerivedViewStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkView(PathLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: RestrictedVar
