from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.facility_requirements_rel_structure import FacilityRequirementsRelStructure
from netex.passenger_capacities_rel_structure import PassengerCapacitiesRelStructure
from netex.passenger_carrying_requirements_rel_structure import PassengerCarryingRequirementsRelStructure
from netex.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.transport_type_version_structure import TransportTypeVersionStructure
from netex.vehicle_manoeuvring_requirements_rel_structure import VehicleManoeuvringRequirementsRelStructure
from netex.vehicle_model_ref_structure import VehicleModelRefStructure
from netex.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeVersionStructure(TransportTypeVersionStructure):
    """
    Type for a VEHICLE TYPE.

    :ivar capacities: Break down of Capacities by FARE CLASS.
    :ivar low_floor: Whether Vehicle is low floor to facilitate access
        by the mobility impaired.
    :ivar has_lift_or_ramp: Whether vehicle has lift or ramp to
        facilitate wheelchair access.
    :ivar has_hoist: Whether vehicle has hoist for wheelchair access.
    :ivar boarding_height: Maximum step height to board. +v1.1
    :ivar gap_to_platform: Expected maximal gap between VEHICLE and
        platform. +v1.1
    :ivar length: The length of a VEHICLE of the type.
    :ivar width: The width of a VEHICLE of the type. +v1.1
    :ivar height: The height of a VEHICLE of the type. +v1.1
    :ivar weight: The weight of a VEHICLE of the type. +v1.1
    :ivar first_axle_height: The height of the first axle of a VEHICLE
        of the type.
    :ivar included_in: Included in definition of VEHICLE.
    :ivar classified_as_ref: Classification of type as being of a
        particular VEHICLE MODEL.
    :ivar facilities: Facilities of VEHICLE TYPE.
    :ivar can_carry: Capacity that VEHICLE TYPE should meet - indicates
        minimum number of seats of each type.
    :ivar can_manoeuvre: Manoeuvring capabilities that VEHICLE TYPE
        should meet.
    :ivar satisfies_facility_requirements: FACILITIES requirements that
        VEHICLE TYPE should meet.
    """
    class Meta:
        name = "VehicleType_VersionStructure"

    capacities: Optional[PassengerCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gap_to_platform: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
    included_in: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "IncludedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    classified_as_ref: Optional[VehicleModelRefStructure] = field(
        default=None,
        metadata={
            "name": "ClassifiedAsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_carry: Optional[PassengerCarryingRequirementsRelStructure] = field(
        default=None,
        metadata={
            "name": "canCarry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    can_manoeuvre: Optional[VehicleManoeuvringRequirementsRelStructure] = field(
        default=None,
        metadata={
            "name": "canManoeuvre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    satisfies_facility_requirements: Optional[FacilityRequirementsRelStructure] = field(
        default=None,
        metadata={
            "name": "satisfiesFacilityRequirements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
