from dataclasses import dataclass

from .operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OperatingPeriod(OperatingPeriodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
