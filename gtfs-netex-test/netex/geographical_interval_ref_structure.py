from dataclasses import dataclass
from .fare_interval_ref_structure import FareIntervalRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalRefStructure(FareIntervalRefStructure):
    value: RestrictedVar
