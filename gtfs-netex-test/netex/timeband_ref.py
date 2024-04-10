from dataclasses import dataclass

from .timeband_ref_structure import TimebandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimebandRef(TimebandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
