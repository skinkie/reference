from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.bay_geometry_enumeration import BayGeometryEnumeration
from netex.multilingual_string import MultilingualString
from netex.parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from netex.parking_capacities_rel_structure import ParkingCapacitiesRelStructure
from netex.parking_ref import ParkingRef
from netex.parking_stay_enumeration import ParkingStayEnumeration
from netex.parking_user_enumeration import ParkingUserEnumeration
from netex.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.parking_visibility_enumeration import ParkingVisibilityEnumeration
from netex.transport_type_refs_rel_structure import TransportTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPropertiesVersionedChildStructure(VersionedChildStructure):
    """
    Type for a PARKING PROPERTies.

    :ivar name: Name of PARKING PROPERTIes.+V1.2.2
    :ivar parking_ref:
    :ivar parking_user_types: Type of users: disabled, all etc.
    :ivar parking_vehicle_types: Type of vehicle that PARKING allows.
    :ivar vehicle_types: TRANSPORT TYPEs  that may use PARKING - open
        codes.  +v1.2.2
    :ivar parking_stay_list: Nature of stay in PARKING.
    :ivar maximum_stay: Maximum allowed Stay as Duration.
    :ivar secure_parking: Whether Parking is secured by surveillance and
        other measures.surveillance.
    :ivar bay_geometry: Relative positioning of Parking bays.  +v1.2.2
    :ivar parking_visibility: Visibible Indication of parking area.
        +v1.2.2
    :ivar areas: PARKING AREA to which prpoerties appky +v1.1.
    :ivar spaces: Available spaces within PARKING AREA.
    """
    class Meta:
        name = "ParkingProperties_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    parking_vehicle_types: List[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    vehicle_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    spaces: Optional[ParkingCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
