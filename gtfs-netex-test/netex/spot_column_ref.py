from dataclasses import dataclass

from .spot_column_ref_structure import SpotColumnRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpotColumnRef(SpotColumnRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
