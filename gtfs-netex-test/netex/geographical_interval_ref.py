from dataclasses import dataclass
from .geographical_interval_ref_structure import (
    GeographicalIntervalRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalRef(GeographicalIntervalRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
