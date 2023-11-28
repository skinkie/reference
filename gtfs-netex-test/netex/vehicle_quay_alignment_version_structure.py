from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.quay_ref import QuayRef
from netex.taxi_stand_ref import TaxiStandRef
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleQuayAlignmentVersionStructure(VersionedChildStructure):
    """
    Type for a VEHICLE QUAY ALIGNMENT.

    :ivar vehicle_stopping_place_ref:
    :ivar taxi_stand_ref_or_quay_ref:
    :ivar order: Order of element.
    """
    class Meta:
        name = "VehicleQuayAlignment_VersionStructure"

    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    taxi_stand_ref_or_quay_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
