from dataclasses import dataclass

from .onward_service_link_derived_view_structure import OnwardServiceLinkDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OnwardServiceLinkView(OnwardServiceLinkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
