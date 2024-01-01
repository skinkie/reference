from dataclasses import dataclass
from .timeband_ref_structure import TimebandRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimebandRef(TimebandRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
