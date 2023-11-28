from dataclasses import dataclass
from netex.operating_period_ref_structure import OperatingPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicOperatingPeriodRef(OperatingPeriodRefStructure):
    """
    Reference to an UIC OPERATING PERIOD.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
