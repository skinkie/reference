from dataclasses import dataclass
from netex.service_access_right_ref_structure import ServiceAccessRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductRefStructure(ServiceAccessRightRefStructure):
    """
    Type for Reference to a FARE PRODUCT.
    """
