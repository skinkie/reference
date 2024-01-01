from dataclasses import dataclass
from .destination_display_derived_view_structure import (
    DestinationDisplayDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayView(DestinationDisplayDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
