from dataclasses import dataclass

from .operating_period_ref_structure import OperatingPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperatingPeriodRef(OperatingPeriodRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
