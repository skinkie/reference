from dataclasses import dataclass
from netex.site_facility_set_ref_structure import SiteFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFacilitySetRef(SiteFacilitySetRefStructure):
    """
    Reference to a SITE FACILITY SET.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
