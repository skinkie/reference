from dataclasses import dataclass

from .spot_row_ref_structure import SpotRowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotRowRef(SpotRowRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
