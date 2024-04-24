from dataclasses import dataclass

from .spot_row_version_structure import SpotRowVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotRow(SpotRowVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
