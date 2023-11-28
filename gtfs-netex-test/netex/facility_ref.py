from dataclasses import dataclass
from netex.facility_ref_structure import FacilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FacilityRef(FacilityRefStructure):
    """
    Reference to a FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
