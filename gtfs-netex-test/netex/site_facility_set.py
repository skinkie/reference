from dataclasses import dataclass, field
from netex.site_facility_set_structure import SiteFacilitySetStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFacilitySet(SiteFacilitySetStructure):
    """
    Set of enumerated FACILITY values that are relevant to a SITE (names based on
    TPEG classifications, augmented with UIC etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
