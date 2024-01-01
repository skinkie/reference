from dataclasses import dataclass
from .destination_display_ref_structure import DestinationDisplayRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayRef(DestinationDisplayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
