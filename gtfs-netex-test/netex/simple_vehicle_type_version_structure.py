from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.licence_requirements_enumeration import LicenceRequirementsEnumeration
from netex.simple_vehicle_category_enumeration import SimpleVehicleCategoryEnumeration
from netex.transport_type_version_structure import TransportTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SimpleVehicleTypeVersionStructure(TransportTypeVersionStructure):
    """
    Type for a PERSONAL TRANSPORT TYPE.

    :ivar length: The length of a VEHICLE of the type.
    :ivar width: The width of a VEHICLE of the type. +v1.1
    :ivar height: The height of a VEHICLE of the type. +v1.1
    :ivar weight: The weight of a VEHICLE of the type. +v1.1
    :ivar first_axle_height: The height of the first axle of a VEHICLE
        of the type.
    :ivar licence_requirements: Licence requirements to use.
    :ivar vehicle_category: Category of vehicle.
    :ivar minimum_age: Minumum age to use TRANSPORT TYPE.
    :ivar portable: Whether vehicle can be carried easily, e.g. scooter,
        skateboard, collapsible bicycle.
    """
    class Meta:
        name = "SimpleVehicleType_VersionStructure"

    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    first_axle_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstAxleHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    licence_requirements: Optional[LicenceRequirementsEnumeration] = field(
        default=None,
        metadata={
            "name": "LicenceRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_category: Optional[SimpleVehicleCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumAge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    portable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Portable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
