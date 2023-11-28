from dataclasses import dataclass, field
from netex.service_facility_set_version_structure import ServiceFacilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySet(ServiceFacilitySetVersionStructure):
    """Service FACILITY.

    Set of enumerated FACILITY values (Where available names are based
    on TPEG classifications, augmented with UIC etc.).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
