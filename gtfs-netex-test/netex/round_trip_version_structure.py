from dataclasses import dataclass, field
from typing import Optional
from netex.round_trip_type_enumeration import RoundTripTypeEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundTripVersionStructure(UsageParameterVersionStructure):
    """
    Type for ROUND TRIP.

    :ivar trip_type: Type of trip. (Single, return, return only).
        default is single.
    :ivar double_single_fare: Whether fare for return trip is simply
        double the single fare.
    :ivar short_trip: Whether trip is classified as a short trip for
        fare calculation.
    :ivar is_required: Whether return trip is required.
    """
    class Meta:
        name = "RoundTrip_VersionStructure"

    trip_type: Optional[RoundTripTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    double_single_fare: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoubleSingleFare",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_trip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShortTrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
