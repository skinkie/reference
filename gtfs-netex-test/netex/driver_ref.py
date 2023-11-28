from dataclasses import dataclass
from netex.driver_ref_structure import DriverRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DriverRef(DriverRefStructure):
    """
    Reference to a DRIVER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
