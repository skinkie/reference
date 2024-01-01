from dataclasses import dataclass
from .destination_display_version_structure import (
    DestinationDisplayVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplay(DestinationDisplayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
