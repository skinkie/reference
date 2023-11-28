from dataclasses import dataclass
from netex.facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySetRefStructure(FacilitySetRefStructure):
    """
    Type for a reference to a SERVICE FACILITY SET.
    """
