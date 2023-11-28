from dataclasses import dataclass, field
from typing import Optional
from netex.transmission_enumeration import TransmissionEnumeration
from netex.vehicle_model_profile_version_structure import VehicleModelProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    """
    Type for a CAR MODEL PROFILE.

    :ivar seats: Number of seats.
    :ivar doors: Number of doors on VEHICLE of VEHICLE MODEL.
    :ivar transmission: Type of gear transmission
    :ivar cruise_control: Whether there is cruise-control
    :ivar sat_nav: Whether VEHICLE has satellite navigation.
    :ivar air_conditioning: Whether VEHICLE has removable chains.
    :ivar convertible: Whether vehicle is convertible
    :ivar usb_power_sockets: Whether VEHICLE has UsbPowerSockets.
    :ivar winter_tyres: Whether VEHICLE has winter tyres.
    :ivar chains: Whether vehicel has remopvable chains.
    :ivar trailer_hitch: Whether VEHICLE has a trailer hitch.
    :ivar roof_rack: WHether VEHICLE has a roof rack.
    :ivar cycle_rack: Whether VEHICLE has a cycle  rack.
    :ivar ski_rack: Whether VEHICLE has a ski rack.
    """
    class Meta:
        name = "CarModelProfile_VersionStructure"

    seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "Seats",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    doors: Optional[int] = field(
        default=None,
        metadata={
            "name": "Doors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transmission: Optional[TransmissionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transmission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cruise_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CruiseControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sat_nav: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SatNav",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    air_conditioning: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AirConditioning",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    convertible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Convertible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usb_power_sockets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UsbPowerSockets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    winter_tyres: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WinterTyres",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    chains: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Chains",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    trailer_hitch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TrailerHitch",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    roof_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RoofRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CycleRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ski_rack: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SkiRack",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
