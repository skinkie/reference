from dataclasses import dataclass, field
from typing import Optional
from netex.multilingual_string import MultilingualString
from netex.vehicle_model_profile_version_structure import VehicleModelProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleModelProfileVersionStructure(VehicleModelProfileVersionStructure):
    """
    Type for a CYCLE MODEL PROFILE.

    :ivar gear_type_descriotion: Description of gearing.
    :ivar battery: Whether there is a Battery
    :ivar lamps: Whether there are lights.
    :ivar helmet: Whether there is a helmet.
    :ivar pump: Whether there is a pump.
    :ivar locker: Whether there is a lockable luggafe container.
    :ivar basket: Whether there is a basket.
    :ivar lock: Whether there is a lock,
    """
    class Meta:
        name = "CycleModelProfile_VersionStructure"

    gear_type_descriotion: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "GearTypeDescriotion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    battery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Battery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lamps: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lamps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    helmet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Helmet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pump: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Locker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    basket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Basket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
