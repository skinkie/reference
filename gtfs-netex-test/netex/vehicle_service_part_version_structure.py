from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.garage_point_ref_structure import GaragePointRefStructure
from netex.multilingual_string import MultilingualString
from netex.vehicle_service_ref import VehicleServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePartVersionStructure(DataManagedObjectStructure):
    """
    Type for VEHICLE SERVICE PART.

    :ivar name: Name of VEHICLE SERVICE PART.
    :ivar description: Description of VEHICLE SERVICE PART.
    :ivar vehicle_service_ref:
    :ivar start_point_ref:
    :ivar end_point_ref:
    """
    class Meta:
        name = "VehicleServicePart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_ref: Optional[VehicleServiceRef] = field(
        default=None,
        metadata={
            "name": "VehicleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[GaragePointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[GaragePointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
