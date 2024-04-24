from dataclasses import dataclass

from .spot_column_version_structure import SpotColumnVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotColumn(SpotColumnVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
