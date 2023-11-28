from dataclasses import dataclass
from netex.service_facility_set_ref_structure import ServiceFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySetRef(ServiceFacilitySetRefStructure):
    """
    Reference to a SERVICE FACILITY SET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
