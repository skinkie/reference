from dataclasses import dataclass, field
from typing import Optional
from netex.log_entry_version_structure import LogEntryVersionStructure
from netex.parking_ref import ParkingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalAvailabilityVersionStructure(LogEntryVersionStructure):
    """
    Type for a RENTAL AVAILABILITY.

    :ivar parking_ref:
    :ivar is_operational: Whether the parking is zurrently operational.
    :ivar is_renting: Whether the parking is currently renting out
        vehicles.
    :ivar is_accepting_returns: Whether the parking is currently
        accepting returned vehicles.
    :ivar available_vehicles: Number of vehicles  available for rental
        at the site.
    :ivar disabled_vehicles: Number of disabled vehicles not available
        for rental at the site.
    :ivar available_docks: Number of docks available to accept vehicle
        returns.
    :ivar disabled_docks: Number of empty but disabled dock points at
        the site.
    """
    class Meta:
        name = "RentalAvailability_VersionStructure"

    parking_ref: ParkingRef = field(
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    is_operational: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsOperational",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_renting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRenting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_accepting_returns: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAcceptingReturns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    available_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "AvailableVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisabledVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    available_docks: Optional[int] = field(
        default=None,
        metadata={
            "name": "AvailableDocks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    disabled_docks: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisabledDocks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
