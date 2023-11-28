from dataclasses import dataclass, field
from netex.passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerInformationFacility:
    """Classification of PASSENGER INFO FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: PassengerInformationFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
