from dataclasses import dataclass

from .destination_display_derived_view_structure import DestinationDisplayDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DestinationDisplayView(DestinationDisplayDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
