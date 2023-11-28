from dataclasses import dataclass
from netex.operating_period_ref_structure import OperatingPeriodRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicOperatingPeriodRefStructure(OperatingPeriodRefStructure):
    """
    Type for a reference to an UIC OPERATING PERIOD.
    """
