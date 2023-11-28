from dataclasses import dataclass, field
from netex.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCommsFacility:
    """Classification of PASSENGER COMMS FACILITY type - TPEG pti23."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: PassengerCommsFacilityEnumeration = field(
        default=PassengerCommsFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
