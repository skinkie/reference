from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.bay_geometry_enumeration import BayGeometryEnumeration
from netex.compound_train_ref import CompoundTrainRef
from netex.parking_area_ref import ParkingAreaRef
from netex.parking_component_version_structure import ParkingComponentVersionStructure
from netex.parking_stay_enumeration import ParkingStayEnumeration
from netex.parking_user_enumeration import ParkingUserEnumeration
from netex.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.parking_visibility_enumeration import ParkingVisibilityEnumeration
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayVersionStructure(ParkingComponentVersionStructure):
    """
    Type for a PARKING BAY.

    :ivar choice:
    :ivar parking_user_types: Type of users: disabled, all etc.
    :ivar parking_vehicle_type: Type of vehicle in PARKING BAY.
    :ivar choice_1:
    :ivar parking_stay_list: Nature of stay in PARKING.
    :ivar maximum_stay: Maximum allowed Stay as Duration.
    :ivar secure_parking: Whether Parking is secured by surveillance and
        other measures.surveillance.
    :ivar bay_geometry: Relative positioning of Parking bays.  +v1.2.2
    :ivar parking_visibility: Visibible Indication of parking area.
        +v1.2.2
    :ivar length: Length of PARKING BAY.
    :ivar width: Width of PARKING BAY.
    :ivar height: Height of PARKING BAY.
    :ivar weight: Maximum Weight allowed in PARKING BAY. +v1.1
    :ivar recharging_available: Whether power for recharging. See
        Equipment for details.
    """
    class Meta:
        name = "ParkingBay_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    parking_user_types: List[ParkingUserEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingUserTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    parking_vehicle_type: Optional[ParkingVehicleEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    parking_stay_list: List[ParkingStayEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingStayList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    maximum_stay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    secure_parking: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SecureParking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bay_geometry: Optional[BayGeometryEnumeration] = field(
        default=None,
        metadata={
            "name": "BayGeometry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_visibility: Optional[ParkingVisibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingVisibility",
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
    recharging_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
